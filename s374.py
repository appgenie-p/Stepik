import re
from typing import List


class Player:
    def __init__(self, name, old, score):
        self.name, self.old, self.score = name, old, score

    def __bool__(self):
        return self.score > 0
    
    def __repr__(self) -> str:
        return f'{self.name}'

# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = [
    'Балакирев; 34; 2048',
    'Mediel; 27; 0',
    'Влад; 18; 9012',
    'Nina P; 33; 0'
    ]

reg = re.compile(r'(\w*\s*\w*);\s(\d+);\s(\d+)')

players = [Player(*reg.match(string).groups()) for string in lst_in]

players_filtered = [ent for ent in players if ent]
