from pydantic import BaseModel


class create_account_dto(BaseModel):
    bank_id: str
    account_type: str
    account_number: str
    product_name: str

class create_bank_dto(BaseModel):
    bank_name: str
    bank_tran_id: str
    bank_code_tran: str
    
class create_transfer_dto(BaseModel):
    account_id: str
    api_tran_date: str
    api_tran_id: str
    bank_tran_code: str
