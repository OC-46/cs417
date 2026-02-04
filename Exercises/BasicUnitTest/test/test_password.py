import pytest
from BasicUnitTest.password import validate_password

def test_validate_password():
    assert validate_password("Password123" == True)

def test_validate_password_boundry():
    assert validate_password("Pass1234" == True)

    assert validate_password("Pas12" == False)