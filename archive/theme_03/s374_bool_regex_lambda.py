import re
import sys
from typing import Tuple


class Player:
    def __init__(self, name: str, old: int, score: int):
        self.name, self.old, self.score = name, old, score

    def __bool__(self):
        return self.score > 0

    def __repr__(self) -> str:
        return f'{self.name}'


def options_prep(string: str) -> Tuple[str, int, int]:
    name, old, score = reg.match(string).groups()
    return name, int(old), int(score)


lst_in = list(map(str.strip, sys.stdin.readlines()))

reg = re.compile(r'(\w*\s*\w*);\s(\d+);\s(\d+)')

players = [Player(*options_prep(string)) for string in lst_in]
players_filtered = list(filter(lambda x: x, players))
