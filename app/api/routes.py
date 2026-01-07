from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.services.logic import check_user_age, InvalidAgeError
from app.repositories.user import UserRepository
from app.dependencies.user import get_user_repository

router = APIRouter()

class AgeRequest(BaseModel):
    age: int

@router.post('/check-age')
def check_age(
    data: AgeRequest,
    repo: UserRepository = Depends(get_user_repository)
):
    result = check_user_age(data.age, repo=repo)
    return {'status': result}
