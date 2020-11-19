import pytest
from user_registration.user_validation import UserRegistration


@pytest.mark.parametrize('user_name, result',
                         [("Yuvraj", True), ("Dhoni", True), ("Ganguly", True), ("Sachin", True),
                          ("yuvraj", "invalid credentials"),
                          ("Dh", "invalid credentials"), ("Ganguly12", "invalid credentials"),
                          ("Sachin?", "invalid credentials"), ("", "entered value is blank")])
def test_for_validating_first_name(user_name, result):
    assert UserRegistration.validate_first_name(user_name) == result


@pytest.mark.parametrize('user_name, result',
                         [("Yuvraj", True), ("Dhoni", True), ("Ganguly", True), ("Sachin", True),
                          ("yuvraj", "invalid credentials"),
                          ("Dh", "invalid credentials"), ("Ganguly12", "invalid credentials"),
                          ("Sachin?", "invalid credentials")])
def test_for_validating_last_name(user_name, result):
    assert UserRegistration.validate_last_name(user_name) == result


@pytest.mark.parametrize('email_id, result',
                         [("abc@yahoo.com", True),
                          ("abc-100@yahoo.com", True),
                          ("abc.100@yahoo.com", True),
                          ("abc111@abc.com", True),
                          ("abc-100@abc.net", True),
                          ("abc.100@abc.com.au", True),
                          ("abc@1.com", True),
                          ("abc@gmail.com.com", True),
                          ("abc+100@gmail.com", True),
                          ("abc", "invalid credentials"),
                          ("abc@.com.my", "invalid credentials"),
                          ("abc123@gmail.a", "invalid credentials"),
                          ("abc123@.com", "invalid credentials"),
                          ("abc123@.com.com", "invalid credentials"),
                          (".abc@abc.com", "invalid credentials"),
                          ("abc()*@gmail.com", "invalid credentials"),
                          ("abc@%*.com", "invalid credentials"),
                          ("abc..2002@gmail.com", "invalid credentials"),
                          ("abc.@gmail.com", "invalid credentials"),
                          ("abc@abc@gmail.com", "invalid credentials"),
                          ("abc@gmail.com.1a", "invalid credentials"),
                          ("abc@gmail.com.aa.au", "invalid credentials")])
def test_for_validating_email_id(email_id, result):
    assert UserRegistration.validate_email_id(email_id) == result


@pytest.mark.parametrize('mobile_number, result',
                         [("91 9851605588", True), ("92 6584122568", True),
                          ("9 9851256598", "invalid credentials"), ("91 67656415", "invalid credentials")])
def test_for_validating_mobile_number(mobile_number, result):
    assert UserRegistration.validate_mobile_number(mobile_number) == result


@pytest.mark.parametrize('password, result',
                         [("Akram@123", True), ("Akram3@Kabir", True),
                          ("Akrhg*98/", "invalid credentials"), ("AkramKabir!", "invalid credentials")])
def test_for_validating_password(password, result):
    assert UserRegistration.validate_password(password) == result
