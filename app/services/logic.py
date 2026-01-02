

def check_user_age(age: int) -> str:
    if age < 18:
        return 'not_allowed'
    return 'allowed'