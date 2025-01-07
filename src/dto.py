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

class get_account_request_dto(BaseModel):
    bank_tran_id: str
    fintech_use_num: str
    tran_dtime: str
    account_number: str

class get_account_response_dto(BaseModel):
    api_tran_id: str
    res_code: str
    rsp_message: str
    api_tran_dtm: str
    bank_tran_id: str
    bank_tran_date: str
    bank_code_tran: str
    bank_rsp_code: str
    bank_rsp_message: str
    fintech_use_num: str
    balance_amt: int
    available_amt: int
    account_type: str
    product_name: str

class get_transfers_request_dto(BaseModel):
    bank_tran_id: str
    account_number: str
    fintech_use_num: str
    inquiry_type: str
    inquiry_base: str
    from_date: str
    from_time: str
    to_date: str
    to_time: str
    sort_order: str
    tran_dtime: str
    before_inquiry_trace_info: str

class transfer_res(BaseModel):
    tran_date: str
    tran_time: str
    inout_type: str
    tran_type: str
    print_content: str
    tran_amt: int
    after_balance_amt: int
    branch_name: str

class get_transfers_response_dto(BaseModel):
    api_tran_id: str
    res_code: str
    res_message: str
    api_tran_dtm: str
    bank_tran_id: str
    bank_tran_date: str
    bank_code_tran: str
    bank_rsp_code: str
    bank_rsp_message: str
    fintech_use_num: str
    balance_amt: int
    page_record_cnt: int
    next_page_yn: str
    before_inquiry_trace_info: str
    res_list: list[transfer_res]
