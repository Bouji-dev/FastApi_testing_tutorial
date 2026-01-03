from app.services.logic import check_user_age


def test_user_age_allowed():
    assert check_user_age(18) == 'allowed'

def test_user_age_not_allowed():
    assert check_user_age(15) == 'not_allowed'

