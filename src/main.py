from fastapi import FastAPI, Depends
from mangum import Mangum
from requests import Session
from dto import create_account_dto
import entity, database
import service

app = FastAPI()

entity.Base.metadata.drop_all(bind=database.engine)        
entity.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def hello() :
	return "안녕하세요! 우아하나 가짜 계정계 서버입니다."

@app.post("/account")
def create_account(dto: create_account_dto, database:Session = Depends(database.get_db)):
	return service.create_account(dto=dto, database=database)

handler = Mangum(app)