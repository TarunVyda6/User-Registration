import pytest
from user_registration.user_validation import UserRegistration


@pytest.mark.parametrize('user_name', [("Yuvraj"), ("Dhoni"), ("Ganguly"), ("Sachin")])
def test_for_valid_first_name(user_name):
    assert UserRegistration.validate_first_name(user_name) == True


@pytest.mark.parametrize('user_name', [("yuvraj"), ("Dh"), ("Ganguly12"), ("Sachin?")])
def test_for_invalid_first_name(user_name):
    assert UserRegistration.validate_first_name(user_name) == False

@pytest.mark.parametrize('user_name', [("Yuvraj"), ("Dhoni"), ("Ganguly"), ("Sachin")])
def test_for_valid_last_name(user_name):
    assert UserRegistration.validate_last_name(user_name) == True


@pytest.mark.parametrize('user_name', [("yuvraj"), ("Dh"), ("Ganguly12"), ("Sachin?")])
def test_for_invalid_last_name(user_name):
    assert UserRegistration.validate_last_name(user_name) == False
