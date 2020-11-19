import re


class UserRegistration:
    @staticmethod
    def validate_first_name(first_name):
        regex = '^[A-Z]{1}[A-Za-z]{2,}$'
        if re.compile(regex).match(first_name):
            return True
        else:
            return False

    @staticmethod
    def validate_last_name(last_name):
        return UserRegistration.validate_first_name(last_name)
