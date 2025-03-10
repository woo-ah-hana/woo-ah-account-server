import datetime
import os
from uuid import uuid4
from dotenv import load_dotenv
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from dto import create_account_dto, create_bank_dto, create_transfer_dto, get_account_request_dto, get_account_response_dto, get_transfers_request_dto, get_transfers_response_dto, response_dto, transfer_res
from entity import Account, Bank, Transfer

load_dotenv()
BASE_URL = os.getenv("FAST_BASE_URL")

def create_bank(dto: create_bank_dto, database:Session):
    new_bank: Bank = Bank(
        id=str(uuid4()),
        bank_name=dto.bank_name,
        bank_tran_id=dto.bank_tran_id,
        bank_code_tran=dto.bank_code_tran
    )

    stmt = select(Bank).where(Bank.bank_name == new_bank.bank_name)
    result = database.execute(stmt)
    existing_bank = result.scalar_one_or_none()

    if existing_bank:
        raise HTTPException(status_code=400, detail="이미 존재하는 은행입니다.")
    database.add(new_bank)
    database.commit()
    database.refresh(new_bank)
    return response_dto(
        is_success=True,
        message="은행을 성공적으로 등록했습니다.",
        data=new_bank
    )

def create_account(dto: create_account_dto, database:Session) -> response_dto:
    new_account: Account = Account(
        id=str(uuid4()),
        bank_tran_id=dto.bank_tran_id,
        account_number=dto.account_number,
        available_amt=0,
        account_type=dto.account_type,
        product_name=dto.product_name,
    )

    stmt = select(Account).where(Account.account_number == new_account.account_number)
    result = database.execute(stmt)
    existing_account = result.scalar_one_or_none()

    if existing_account:
        raise HTTPException(status_code=400, detail="이미 존재하는 계좌번호입니다.")

    database.add(new_account)
    database.commit()
    database.refresh(new_account)

    return response_dto(
        is_success=True,
        message="성공적으로 계좌를 등록했습니다.",
        data=new_account
    )

def create_transfer(dto: create_transfer_dto, database: Session)-> response_dto:
    account = database.query(Account).filter(Account.account_number==dto.account_number).first()
    if not account:
        raise HTTPException(status_code=404, detail="해당 계좌번호를 찾을 수 없습니다.")
    
    if(dto.inout_type == "출금" and (account.available_amt >= dto.tran_amt)):
        after_amt = account.available_amt - dto.tran_amt
    elif(dto.inout_type == "출금" and (account.available_amt < dto.tran_amt)):
        raise HTTPException(status_code=403, detail="잔액이 부족합니다.")
    elif(dto.inout_type == "입금"):
        after_amt = account.available_amt + dto.tran_amt
    else:
        raise HTTPException(status_code=400, detail="(입출금)잘못된 접근입니다.")
    account.available_amt = after_amt
    database.add(account)
    trans_date = datetime.datetime.strptime(dto.tran_date, "%Y-%m-%d").date()
    print(trans_date)
    transfer = Transfer(
        id=str(uuid4()),
        account_number = dto.account_number,
        tran_date = trans_date,
        tran_time = dto.tran_time,
        inout_type = dto.inout_type,
        tran_type = dto.tran_type,
        print_content = dto.print_content,
        tran_amt = dto.tran_amt,
        after_balance_amt = after_amt,
        branch_name = dto.branch_name
    )
    database.add(transfer)

    try:
        database.commit()  # 모든 데이터가 성공적으로 저장되면 트랜잭션을 커밋

        return response_dto(
            is_success=True,
            message="거래가 성공적으로 완료되었습니다.",
            data=after_amt
        )
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=500, detail="거래에 실패했습니다. 원인:"+error)
    

def get_account(dto: get_account_request_dto, database: Session)-> response_dto:
    account = database.query(Account).filter(Account.account_number==dto.account_number).first()
    bank = database.query(Bank).filter(Bank.bank_tran_id == dto.bank_tran_id).first()

    if not account: raise HTTPException(status_code=404, detail="해당 계좌를 찾을 수 없습니다.")
    if not bank: raise HTTPException(status_code=404, detail="지원하지 않는 은행코드입니다.")
    
    try:
        acc_response = get_account_response_dto(
            api_tran_id="0",
            res_code="0",
            rsp_message="성공적으로 계좌를 불러왔습니다.",
            api_tran_dtm="0",
            bank_tran_id=dto.bank_tran_id,
            bank_tran_date="0",
            bank_code_tran=bank.bank_name,
            bank_rsp_code="0",
            bank_rsp_message="성공적으로 계좌를 불러왔습니다.",
            fintech_use_num=dto.fintech_use_num,
            balance_amt=account.available_amt,
            available_amt=account.available_amt,
            account_type=account.account_type,
            product_name=account.product_name)

        return response_dto(is_success=True, message="성공적으로 계좌를 불러왔습니다.", data=acc_response)
    
    except Exception as error:
        database.rollback() 
        raise HTTPException(status_code=500, detail="알 수 없는 에러가 발생했습니다. 원인:"+error)

def get_transfers(dto: get_transfers_request_dto, database: Session)-> response_dto:
    account = database.query(Account).filter(Account.account_number==dto.account_number).first()
    if not account: raise HTTPException(status_code=404, detail="해당 계좌를 찾을 수 없습니다.")

    start_date = datetime.datetime.strptime(dto.from_date, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(dto.to_date, "%Y-%m-%d").date()
    if start_date > end_date: raise HTTPException(status_code=400, detail="조회 시작 날짜가 조회 끝 날자보다 앞섭니다.")
    
    try:
        query = select(Transfer).where(Transfer.account_number == account.account_number,(Transfer.tran_date >= start_date) & (Transfer.tran_date <= end_date))
        result = database.execute(query)
        transfers = result.scalars().all()

        transfer_list: list[transfer_res] = []
        for transfer in transfers:
            item = transfer_res(
                tran_date= str(transfer.tran_date),
                tran_time= transfer.tran_time,
                inout_type=transfer.inout_type,
                tran_type=transfer.tran_type,
                print_content=transfer.print_content,
                tran_amt=transfer.tran_amt,
                after_balance_amt=transfer.after_balance_amt,
                branch_name=transfer.branch_name
            )
            transfer_list.append(item)

        result = get_transfers_response_dto(
            api_tran_id="0",
            res_code="0",
            res_message="성공적으로 거래내역을 불러왔습니다.",
            api_tran_dtm="0",
            bank_tran_id=dto.bank_tran_id,
            bank_tran_date="",
            bank_code_tran=dto.bank_tran_id+"U12345",
            bank_rsp_code="",
            bank_rsp_message="",
            fintech_use_num=dto.fintech_use_num,
            balance_amt=account.available_amt,
            page_record_cnt=len(transfer_list),
            next_page_yn="no",
            before_inquiry_trace_info="",
            res_list=transfer_list
        )

        return response_dto(
            is_success=True,
            message="성공적으로 거래내역을 불러왔습니다.",
            data=result
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail="알 수 없는 에러가 발생했습니다. 원인: "+error)


    