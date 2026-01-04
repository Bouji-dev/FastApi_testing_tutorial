from app.models.user import UserCreate
from app.repositories.user import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: UserCreate):
        return self.repository.create(user)
        

def check_user_age(age: int) -> str:
    if age < 18:
        return 'not_allowed'
    return 'allowed'

