from app.models.user import UserCreate
from app.repositories.user import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: UserCreate):
        return self.repository.create(user)
        
class InvalidAgeError(Exception):
    pass


def check_user_age(age: int) -> str:
    if age < 0:
        raise InvalidAgeError('age must be non-negative')
    return 'allowed' if age >= 18 else 'not_allowed'