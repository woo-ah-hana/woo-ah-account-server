from fastapi import FastAPI, Depends
from mangum import Mangum
from requests import Session
from dto import create_account_dto, create_bank_dto, create_transfer_dto
import entity, database
import service

app = FastAPI()

entity.Base.metadata.drop_all(bind=database.engine)        
entity.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def hello() :
	return "안녕하세요! 우아하나 가짜 계정계 서버입니다."

@app.post("/bank")
def create_bank(dto: create_bank_dto, database:Session = Depends(database.get_db)):
	
	return service.create_bank(dto=dto, database=database)

@app.post("/account")
def create_account(dto: create_account_dto, database:Session = Depends(database.get_db)):
	return service.create_account(dto=dto, database=database)

@app.post("/transfer")
def create_transfer(dto: create_transfer_dto, database:Session = Depends(database.get_db)):
	return service.create_transfer(dto=dto, database=database)



handler = Mangum(app)