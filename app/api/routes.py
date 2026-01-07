from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.logic import check_user_age, InvalidAgeError
from app.repositories.user import UserRepository

router = APIRouter()

class AgeRequest(BaseModel):
    age: int

@router.post('/check-age')
def check_age(data: AgeRequest):
    
    repo = UserRepository()
    try:
        result = check_user_age(data.age, repo=repo)
        return {'status': result}
    except InvalidAgeError as e:
        raise HTTPException(status_code=400, detail=str(e))