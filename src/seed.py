from uuid import uuid4

from database import SessionLocal
from entity import Bank, Account, Transfer

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

            # 테스트용 계좌
            Account(id=str(uuid4()), bank_tran_id="004", account_number="1601823391973", available_amt=1515000, account_type="0", product_name="자유입출금계좌"),  # 김민지
            Account(id=str(uuid4()), bank_tran_id="005", account_number="0168966238333", available_amt=2432000, account_type="0", product_name="자유입출금계좌"),  # 팜하니
            Account(id=str(uuid4()), bank_tran_id="004", account_number="1606917992650", available_amt=1702000, account_type="0", product_name="자유입출금계좌"),  # 강해린
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468974443067", available_amt=2348000, account_type="0", product_name="자유입출금계좌"),  # 다니엘
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468299555144", available_amt=1262000, account_type="0", product_name="자유입출금계좌"),  # 이혜인
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1462685112064", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1464500439558", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1462919942347", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),

            # 모임통장 계좌
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468152645150", available_amt=2451430, account_type="0", product_name="자유입출금계좌"), # 맛집탐방, 계주 : 함형주
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1463056220188", available_amt=4216300, account_type="0", product_name="자유입출금계좌"), # 떠나요 여행, 계주 : 안유진
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1464493512314", available_amt=862000, account_type="0", product_name="자유입출금계좌"), # 가방, 계주 : 윤영헌
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1465510634457", available_amt=1250000, account_type="0", product_name="자유입출금계좌"), # 가평가자, 계주 : 김미강

            # 예비용 : 모임 개설 시에 사용(하나은행 계좌만)
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468214722317", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1469416055289", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1468645396450", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1465938219017", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),

            # 예비용 : 회원가입 시에 사용
            Account(id=str(uuid4()), bank_tran_id="001", account_number="1463387516144", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="002", account_number="3561427886421", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="003", account_number="2150421166735", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="004", account_number="1606724457286", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),
            Account(id=str(uuid4()), bank_tran_id="005", account_number="0167542228614", available_amt=1200000, account_type="0", product_name="자유입출금계좌"),

        ]

        transfer = [
            # 거래 내역
            # 모임 1번(맛집탐방) - 계획 1번(수리고등학교 동창 강릉 여행), 계주 : 함형주, 최초 잔액 : 3257500
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-10", tran_time="09:30",
                     inout_type="출금", tran_type="결재", print_content="스타벅스 성수역점", tran_amt="22400", after_balance_amt="3212700",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-10", tran_time="12:35",
                     inout_type="출금", tran_type="결재", print_content="동화가든", tran_amt="84000", after_balance_amt="3128700",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-10", tran_time="14:08",
                     inout_type="출금", tran_type="결재", print_content="카페 툇마루", tran_amt="42000", after_balance_amt="3086700",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-10", tran_time="19:27",
                     inout_type="출금", tran_type="결재", print_content="강릉다물선횟집", tran_amt="165000", after_balance_amt="2921700",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-10", tran_time="21:15",
                     inout_type="출금", tran_type="결재", print_content="CU경포비치점", tran_amt="25750", after_balance_amt="2895950",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-11", tran_time="09:48",
                     inout_type="출금", tran_type="결재", print_content="교동짬뽕 강릉본점", tran_amt="64000", after_balance_amt="2831950",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-11", tran_time="10:25",
                     inout_type="출금", tran_type="결재", print_content="오죽헌입장료", tran_amt="18000", after_balance_amt="2813950",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-11", tran_time="14:08",
                     inout_type="출금", tran_type="결재", print_content="카페 뤼미에르", tran_amt="21000", after_balance_amt="2792950",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-11", tran_time="16:04",
                     inout_type="출금", tran_type="결재", print_content="강릉수제어묵고로케", tran_amt="45000", after_balance_amt="2747950",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-11", tran_time="19:58",
                     inout_type="출금", tran_type="결재", print_content="금학칼국수", tran_amt="58000", after_balance_amt="2689950",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-11", tran_time="20:30",
                     inout_type="출금", tran_type="결재", print_content="홈플러스 강릉점", tran_amt="37520", after_balance_amt="2652430",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-12", tran_time="08:17",
                     inout_type="출금", tran_type="결재", print_content="이마트24 강문해변점", tran_amt="12000", after_balance_amt="2640430",
                     branch_name=""),

            # 모임 1번(맛집탐방) - 계획 2번(성수 나들이), 계주 : 함형주, 최초 잔액 : 2640430
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-15", tran_time="10:17",
                     inout_type="출금", tran_type="결재", print_content="자연도소금빵", tran_amt="12000", after_balance_amt="2628430",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-15", tran_time="13:10",
                     inout_type="출금", tran_type="결재", print_content="소문난성수감자탕", tran_amt="57000", after_balance_amt="2571430",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-15", tran_time="14:17",
                     inout_type="출금", tran_type="결재", print_content="무신사스탠다드성수점", tran_amt="99000", after_balance_amt="2472430",
                     branch_name=""),
            Transfer(id=str(uuid4()), account_number="1468152645150", tran_date="2025-01-15", tran_time="14:48",
                     inout_type="출금", tran_type="결재", print_content="스타벅스성수역점", tran_amt="21000", after_balance_amt="2451430",
                     branch_name=""),

        ]

        db.add_all(bank)
        db.add_all(account)
        db.add_all(transfer)
        db.commit()
        print("seeding completed")

    except Exception as e :
        print(f"데이터 시딩 중 오류 발생 : {e}")
    finally :
        db.close()