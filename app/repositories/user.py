from app.models.user import UserCreate


class UserRepository:
    def create(self, user: UserCreate):
        raise NotImplementedError