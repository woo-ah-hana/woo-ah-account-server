from pydantic import BaseModel

class response_dto(BaseModel):
    is_success: bool
    message: str
    data: object

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
    account_number: str
    tran_date: str
    tran_time: str
    inout_type: str
    tran_type: str
    print_content: str
    tran_amt: int
    branch_name: str
    # 여기부터는 mock 처리
    api_tran_dtm: str
    api_tran_id: str
    bank_tran_id: str
    bank_code_tran: str
    bank_rsp_code: str
    fintech_use_num: str
    befor_inquiry_trace_info: str
