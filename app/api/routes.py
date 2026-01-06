from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.logic import check_user_age, InvalidAgeError

router = APIRouter()

class AgeRequest(BaseModel):
    age: int


# @router.post("/check-age")
# def check_age(data: AgeRequest):
#     result = check_user_age(data.age)
#     return {"status": result}


@router.post('/check-age')
def check_age(data: AgeRequest):
    try:
        result = check_user_age(data.age)
        return {'status': result}
    except InvalidAgeError as e:
        raise HTTPException(status_code=400, detail=str(e))