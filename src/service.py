import os
from uuid import uuid4
from dotenv import load_dotenv
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from dto import create_account_dto
from entity import Account

load_dotenv()
BASE_URL = os.getenv("FAST_BASE_URL")

def create_account(dto: create_account_dto, database:Session) -> Account:
    new_account: Account = Account(
        id=str(uuid4()),
        bank_id=dto.bank_id,
        account_number=dto.account_number,
        available_amt="0", 
        account_type=dto.account_type,
        product_name=dto.product_name,
    )

    stmt = select(Account).where(Account.account_number == new_account.account_number)
    result = database.execute(stmt)
    existing_account = result.scalar_one_or_none()

    if existing_account:
        raise HTTPException(status_code=400, detail="Account number already exists")

    database.add(new_account)
    database.commit()
    database.refresh(new_account)

    return new_account