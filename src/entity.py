from uuid import uuid4
from sqlalchemy import Column, UUID, String
from database import Base

class Bank(Base):
    __tablename__ = "bank"

    id = Column(String, primary_key=True, default=str(uuid4()))
    bank_name = Column(String(50), index=True, unique=True)
    bank_tran_id = Column(String(50), index=True)
    bank_code_tran = Column(String(50), index=True)

class Account(Base):
    __tablename__ = "account"

    id = Column(String(50), primary_key=True, default=str(uuid4()))
    bank_id = Column(String(50), index=True)
    account_number = Column(String(50), index=True, unique=True)
    available_amt = Column(String(50), index=True)
    account_type = Column(String(50), index=True)
    product_name = Column(String(50), index=True)

class Transfer(Base):
    __tablename__ = "transfer"
    
    id = Column(String, primary_key=True, default=str(uuid4()))
    account_id = Column(String(50), index=True)
    tran_date = Column(String(50), index=True)
    tran_time = Column(String(50), index=True)
    inout_type = Column(String(50), index=True)
    tran_type = Column(String(50), index=True)
    print_content = Column(String(50), index=True)
    tran_amt = Column(String(50), index=True)
    after_balance_amt = Column(String(50), index=True)
    branch_name = Column(String(50), index=True)