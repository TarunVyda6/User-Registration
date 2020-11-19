import pytest
from user_registration.user_validation import UserRegistration


@pytest.mark.parametrize('user_name, result',
                         [("Yuvraj", True), ("Dhoni", True), ("Ganguly", True), ("Sachin", True), ("yuvraj", False),
                          ("Dh", False), ("Ganguly12", False), ("Sachin?", False)])
def test_for_validating_first_name(user_name, result):
    assert UserRegistration.validate_first_name(user_name) == result


@pytest.mark.parametrize('user_name, result',
                         [("Yuvraj", True), ("Dhoni", True), ("Ganguly", True), ("Sachin", True), ("yuvraj", False),
                          ("Dh", False), ("Ganguly12", False), ("Sachin?", False)])
def test_for_validating_last_name(user_name, result):
    assert UserRegistration.validate_last_name(user_name) == result


@pytest.mark.parametrize('email_id, result',
                         [("abc@yahoo.com", True), ("abc-100@yahoo.com", True), ("abc.100@yahoo.com", True),
                          ("abc111@abc.com", True),
                          ("abc-100@abc.net", True), ("abc.100@abc.com.au", True), ("abc@1.com", True),
                          ("abc@gmail.com.com", True),
                          ("abc+100@gmail.com", True), ("abc", False),
                          ("abc@.com.my", False),
                          ("abc123@gmail.a", False),
                          ("abc123@.com", False),
                          ("abc123@.com.com", False),
                          (".abc@abc.com", False),
                          ("abc()*@gmail.com", False),
                          ("abc@%*.com", False),
                          ("abc..2002@gmail.com", False),
                          ("abc.@gmail.com", False),
                          ("abc@abc@gmail.com", False),
                          ("abc@gmail.com.1a", False),
                          ("abc@gmail.com.aa.au", False)])
def test_for_validating_email_id(email_id, result):
    assert UserRegistration.validate_email_id(email_id) == result
