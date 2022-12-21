class ValidatorString:
    def __init__(self, min_length: int, max_length: int, chars: str):
        # Если chars пустая строка,  проверку на вхождение символов не делать.
        self.min_length = min_length
        self.max_length = max_length

    def is_valid(self, string: str) -> bool:
        pass


class LoginForm:
    def __init__(self, login_validator: ValidatorString,
                 password_validator: ValidatorString) -> None:
        self.login_validator = login_validator
        self.password_validator = password_validator
