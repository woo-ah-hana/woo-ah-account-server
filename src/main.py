from fastapi import FastAPI
from mangum import Mangum
import entity, database

app = FastAPI()

entity.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def hello() :
	return "안녕하세요! 우아하나 가짜 계정계 서버입니다."


handler = Mangum(app)