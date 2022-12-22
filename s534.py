from typing import Dict, Optional


class ValidatorString:
    def __init__(self, min_length: int, max_length: int, chars: str):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string: Optional[str]) -> bool:
        if all([
            type(string) == str,
            self.min_length <= len(string) <= self.max_length,
            any(symbol for symbol in string if symbol in self.chars) if len(
                self.chars) != 0 else True,
        ]):
            return True

        raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator: ValidatorString,
                 password_validator: ValidatorString,):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request: Dict[str, str]) -> None:
        if not all([request.get('login'), request.get('password')]):
            raise TypeError('в запросе отсутствует логин или пароль')
        if self.login_validator.is_valid(request.get('login')):
            self._login = request.get('login')
        if self.password_validator.is_valid(request.get('password')):
            self._password = request.get('password')


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = "sergey balakirev!".split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
