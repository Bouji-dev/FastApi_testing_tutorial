from app.services.logic import check_user_age, UserService
from app.models.user import UserCreate



def test_user_age_allowed():
    assert check_user_age(18) == 'allowed'

def test_user_age_not_allowed():
    assert check_user_age(15) == 'not_allowed'

class FakeUserRepository:
    def create(self, user):
        return user
    

def test_user_service_create_user():
    repo = FakeUserRepository()
    service = UserService(repo)

    user = UserCreate(username='Ehsan', age=30)
    result = service.create_user(user)

    assert result.username == 'Ehsan'
    assert result.age == 30