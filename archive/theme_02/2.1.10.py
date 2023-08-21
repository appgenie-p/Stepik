import re
from random import choice, randint
from string import ascii_lowercase, digits


class EmailValidator:
    def __new__(cls):
        return None

    @classmethod
    def get_random_email(cls):
        mail_letters = ascii_lowercase
        mail_digits = digits
        chars = f"{mail_letters}{mail_digits}_."
        email_length = randint(1, 100)
        email_name = "".join(choice(chars) for i in range(email_length + 1))
        return f"{email_name}@gmail.com"

    @classmethod
    def check_email(cls, email) -> bool:
        """- возвращает True, если email записан верно и False - в противном
        случае.
        """
        if not cls.__is_email_str(email):
            return False
        email_regex = r"(?!.*\.\.)[\w\.]{1,100}@(?=.*\..*)[\w\.]{1,50}"
        res = re.fullmatch(email_regex, email)
        if res:
            return True
        return False

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


# res = EmailValidator.__is_email_str('abc')
# print(res)
# res = EmailValidator.check_email("sc_lib@list.ru")      # True
# print(res)
# res = EmailValidator.check_email("sc_lib@list_ru")      # False
# print(res)
# res = EmailValidator.get_random_email()
# print(res)
