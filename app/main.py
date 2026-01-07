from fastapi import FastAPI, Request
from app.models.user import UserCreate
from app.api.routes import router
from fastapi.responses import JSONResponse
from app.services.logic import InvalidAgeError

app = FastAPI()
app.include_router(router)


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

@app.exception_handler(InvalidAgeError)
def invalid_age_exception_handler(
    request: Request,
    exc: InvalidAgeError,
):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )