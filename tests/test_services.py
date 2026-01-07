from app.services.logic import check_user_age, UserService
from app.models.user import UserCreate
from unittest.mock import Mock

class FakeUserRepository:
    def create(self, user):
        return user
    

def test_user_age_allowed():
    repo = Mock()
    assert check_user_age(18, repo=repo) == 'allowed'

def test_user_age_not_allowed():
    repo = Mock()
    assert check_user_age(15, repo=repo) == 'not_allowed'


def test_user_service_create_user():
    repo = FakeUserRepository()
    service = UserService(repo)

    user = UserCreate(username='Ehsan', age=30)
    result = service.create_user(user)

    assert result.username == 'Ehsan'
    assert result.age == 30

def test_age_zero():
    repo = Mock()
    assert check_user_age(0, repo=repo) == 'not_allowed'

def test_age_boundary_age():
    repo = Mock()
    assert check_user_age(18, repo=repo) == 'allowed'

def test_age_very_large():
    repo = Mock()
    assert check_user_age(200, repo=repo) == 'allowed'        

def test_check_user_age_calls_repository():
    fake_repo = Mock()

    result = check_user_age(20, repo=fake_repo)

    fake_repo.save.assert_called_once_with(20)
    assert result == 'allowed'