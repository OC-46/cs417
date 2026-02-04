#password valitdator

def validate_password(password:str):

    if password is float or int:
        raise TypeError
    
    if len(password) < 8:
        return False
    
    has_uppercase = any(val.isupper() for val in password)
    has_num = any(val.isdigit() for val in password)
    return has_uppercase and has_num