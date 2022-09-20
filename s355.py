

import re
from typing import List, Sequence


stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__(self, lst_words: Sequence[str]) -> None:
        self.lst_words = lst_words

    def __repr__(self):
        return f"{' '.join(self.lst_words)}"

lst_text = []
for string in stich:
    raw_words = string.split()
    lst_text.append(
        StringText([a for word in raw_words 
        if len(
            a := re.sub(r"[?!,.;–]", '', word)
        ) > 0])
    )

pass