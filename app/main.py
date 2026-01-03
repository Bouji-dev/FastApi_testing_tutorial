from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    age: int

@app.get('/')
async def read_root():
    return {'message': 'Hello World'}

@app.get('/ping')
async def get_ping():
    return {'status': 'ok'}

@app.get('/hello')
async def hello(name: str | None = 'Anonymous'):
    return {'message': f'Hello {name}'}

@app.post('/users')
async def create_user(user: UserCreate):
    return user