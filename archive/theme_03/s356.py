from typing import Tuple


class Morph:
    def __init__(self, *args) -> None:
        self.words = list(args)

    def add_word(self, word: str) -> None:
        self.words.append(word)

    def get_words(self) -> Tuple[str, ...]:
        return tuple(self.words)

    def __eq__(self, comparable: str) -> bool:
        return any(
            comparable.lower().strip(".,?!-") == word.lower() for word in self.words
        )

    def __req__(self, comparable) -> bool:
        return self == comparable


# text = 'Мы будем устанавливать связь завтра днем.'
text = input()

dict_words = [
    Morph("связь", "связи", "связью", "связи", "связей", "связям", "связями", "связях"),
    Morph(
        "формула",
        "формулы",
        "формуле",
        "формулу",
        "формулой",
        "формул",
        "формулам",
        "формулами",
        "формулах",
    ),
    Morph(
        "вектор",
        "вектора",
        "вектору",
        "вектором",
        "векторе",
        "векторы",
        "векторов",
        "векторам",
        "векторами",
        "векторах",
    ),
    Morph(
        "эффект",
        "эффекта",
        "эффекту",
        "эффектом",
        "эффекте",
        "эффекты",
        "эффектов",
        "эффектам",
        "эффектами",
        "эффектах",
    ),
    Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях"),
]

counter = 0
for word in text.split():
    if word.strip(".,?!-") in dict_words:
        counter += 1
print(counter)

for mw in dict_words:
    assert mw != "связ", "некорректно работает оператор != с объектами класса Morph"
