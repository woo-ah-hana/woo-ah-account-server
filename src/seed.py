from uuid import uuid4

from database import SessionLocal
from entity import Bank, Account

def data_seed() :
    db = SessionLocal()
    try :
        if db.query(Bank).first() :
            print("중복 데이터")
            return

        bank = [
            # 은행 목록
            Bank(id=str(uuid4()), bank_name="하나은행", bank_tran_id="001", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="농협은행", bank_tran_id="002", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="우리은행", bank_tran_id="003", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="신한은행", bank_tran_id="004", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="기업은행", bank_tran_id="005", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="카카오뱅크", bank_tran_id="006", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="토스뱅크", bank_tran_id="007", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="KB국민은행", bank_tran_id="008", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="부산은행", bank_tran_id="009", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="대구은행", bank_tran_id="010", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="광주은행", bank_tran_id="011", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="전북은행", bank_tran_id="012", bank_code_tran="097U12345"),
            Bank(id=str(uuid4()), bank_name="제주은행", bank_tran_id="013", bank_code_tran="097U12345")
        ]

        account = [
            # 개인 계좌
            Account(id=str(uuid4()), bank_tran_id="002", account_number="3561057204496", available_amt=1821000, account_type="0", product_name="자유입출금계좌"), # 함형주
            Account(id=str(uuid4()), bank_tran_id="003", account_number="2150094621845", available_amt=2632000, account_type="0", product_name="자유입출금계좌"), # 최선정
            Account(id=str(uuid4()), bank_tran_id="002", account_number="3561024215509", available_amt=2543000, account_type="0", product_name="자유입출금계좌"), # 윤영헌
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1462665915101", available_amt=2634000, account_type="0", product_name="자유입출금계좌"), # 김상현
            Account(id=str(uuid4()), bank_tran_id="005", account_number="0181011629531", available_amt=1825000, account_type="0", product_name="자유입출금계좌"), # 김채운
            Account(id=str(uuid4()), bank_tran_id="006", account_number="3333057204496", available_amt=1716000, account_type="0", product_name="자유입출금계좌"), # 김미강
            Account(id=str(uuid4()), bank_tran_id="002", account_number="3561084512201", available_amt=1557000, account_type="0", product_name="자유입출금계좌"), # 안유진
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1464397169654", available_amt=2248000, account_type="0", product_name="자유입출금계좌"), # 김가을
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1467018418840", available_amt=1139000, account_type="0", product_name="자유입출금계좌"), # 장원영
            Account(id=str(uuid4()), bank_tran_id="008", account_number="5215712291290", available_amt=1540000, account_type="0", product_name="자유입출금계좌"), # 김레이
            Account(id=str(uuid4()), bank_tran_id="009", account_number="1728638574889", available_amt=2151000, account_type="0", product_name="자유입출금계좌"), # 김지원
            Account(id=str(uuid4()), bank_tran_id="010", account_number="2662280371228", available_amt=762000, account_type="0", product_name="자유입출금계좌"), # 이현서
            Account(id=str(uuid4()), bank_tran_id="004", account_number="1601823391973", available_amt=1515000, account_type="0", product_name="자유입출금계좌"),  # 김민지
            Account(id=str(uuid4()), bank_tran_id="005", account_number="0168966238333", available_amt=2432000, account_type="0", product_name="자유입출금계좌"),  # 팜하니
            Account(id=str(uuid4()), bank_tran_id="004", account_number="1606917992650", available_amt=1702000, account_type="0", product_name="자유입출금계좌"),  # 강해린
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468974443067", available_amt=2348000, account_type="0", product_name="자유입출금계좌"),  # 다니엘
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468299555144", available_amt=1262000, account_type="0", product_name="자유입출금계좌"),  # 이혜인

            # 모임통장 계좌
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468152645150", available_amt=3257500, account_type="0", product_name="자유입출금계좌"), # 맛집탐방, 계주 : 함형주
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1463056220188", available_amt=4216300, account_type="0", product_name="자유입출금계좌"), # 떠나요 여행, 계주 : 안유진
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1464493512314", available_amt=862000, account_type="0", product_name="자유입출금계좌"), # 가방, 계주 : 윤영헌
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1465510634457", available_amt=1250000, account_type="0", product_name="자유입출금계좌"), # 가평가자, 계주 : 김미강

            # 예비용 : 모임 개설 시에 사용
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1462685112064", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1464500439558", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1462919942347", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468214722317", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1469416055289", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468645396450", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1465938219017", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),

            # 예비용 : 회원가입 시에 사용
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1462685112064", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="002", account_number="3561427886421", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="003", account_number="2150421166735", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="004", account_number="1606724457286", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="005", account_number="0167542228614", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),

        ]

        db.add_all(bank)
        db.add_all(account)
        db.commit()
        print("seeding completed")

    except Exception as e :
        print(f"데이터 시딩 중 오류 발생 : {e}")
    finally :
        db.close()