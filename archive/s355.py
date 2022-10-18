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

    def __repr__(self) -> str:
        return f"{' '.join(self.lst_words)}"

    def __len__(self) -> int:
        return len(self.lst_words)

    def __gt__(self, comparable: 'StringText') -> bool:
        return len(self) > len(comparable)
    
    def __ge__(self, comparable: 'StringText') -> bool:
        return len(self) >= len(comparable)


lst_text = []
for string in stich:
    raw_words = string.split()
    lst_text.append(
        StringText(
            [re.sub(r"[?!,.;–]", '', word) for word in raw_words 
            if len(re.sub(r"[?!,.;–]", '', word)) > 0]
        )
    )

lst_text_sorted = [repr(phrase) for phrase in sorted(lst_text, reverse=True)]