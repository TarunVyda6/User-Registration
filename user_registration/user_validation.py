import re


class UserRegistration:
    @staticmethod
    def validate_first_name(name):
        regex = '^[A-Z]{1}[A-Za-z]{2,}$'
        return UserRegistration.check_regex(regex, name)

    @staticmethod
    def validate_last_name(name):
        return UserRegistration.validate_first_name(name)

    @staticmethod
    def validate_email_id(email_id):
        regex = '^[a-zA-Z]{3,}[0-9]{0,}([-._+]{1}[a-zA-Z0-9]{3,})?@[a-zA-Z0-9]{1,}[.]{1}[a-zA-Z]{3}(.[a-zA-z]{2,4})?$'
        return UserRegistration.check_regex(regex, email_id)

    @staticmethod
    def check_regex(regex, user_detail):
        if re.compile(regex).match(user_detail):
            return True
        else:
            return False
