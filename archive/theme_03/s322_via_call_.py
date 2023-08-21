from typing import Any

from random import randint, choices


class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pswd_len = randint(self.min_length, self.max_length)
        return "".join(choices(self.psw_chars, k=pswd_len))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)

lst_pass = [rnd() for _ in range(3)]
print(lst_pass)
