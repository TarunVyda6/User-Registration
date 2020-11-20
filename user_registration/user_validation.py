import re
from user_registration.user_details_exception import *


class UserRegistration:
    @staticmethod
    def validate_first_name(name):
        """
        validates first name
        :param name: takes first name as input
        :return: True if pattern matches and returns invalid credentials exception if it doesn't match
        """
        regex = '^[A-Z]{1}[A-Za-z]{2,}$'
        return UserRegistration.check_regex(regex, name)

    @staticmethod
    def validate_last_name(name):
        """
        validates last name
        :param name: takes last name as input
        :return: True if pattern matches and returns invalid credentials exception if it doesn't match
        """
        return UserRegistration.validate_first_name(name)

    @staticmethod
    def validate_email_id(email_id):
        """
        validates email id
        :param email_id: takes email id as input
        :return: True if pattern matches and returns invalid credentials exception if it doesn't match
        """
        regex = '^[a-zA-Z]{3,}[0-9]{0,}([-._+]{1}[a-zA-Z0-9]{3,})?@[a-zA-Z0-9]{1,}[.]{1}[a-zA-Z]{3}(.[a-zA-z]{2,4})?$'
        return UserRegistration.check_regex(regex, email_id)

    @staticmethod
    def validate_mobile_number(mobile_number):
        """
        validates mobile number
        :param mobile_number: takes mobile number as input
        :return: True if pattern matches and returns invalid credentials exception if it doesn't match
        """
        regex = '^[0-9]{2,3} [0-9]{10}$'
        return UserRegistration.check_regex(regex, mobile_number)

    @staticmethod
    def validate_password(password):
        """
        validates password
        :param password: takes password as input
        :return: True if pattern matches and returns invalid credentials exception if it doesn't match
        """
        regex = '^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}'
        return UserRegistration.check_regex(regex, password)

    @staticmethod
    def check_regex(regex, user_detail):
        """
        takes user detail as input and checks for exception and regex pattern matching
        :param regex: takes regex expression as one of the input
        :param user_detail: takes users information as another input
        :return: True if pattern matches and returns invalid credentials exception if it doesn't match
        """
        try:
            if user_detail == "":
                raise NoValueException("entered value is blank")
        except NoValueException as e:
            return e.message
        try:
            if not re.compile(regex).match(user_detail):
                raise InvalidCredentialsException("invalid credentials")
            else:
                return True
        except InvalidCredentialsException as e:
            return e.message
