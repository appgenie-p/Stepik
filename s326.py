from typing import List


class RenderList:
    def __init__(self, type_list: str = 'ul'):
        self.type_list = type_list

    def __call__(self, lst: List[str]) -> str:
        return (f'<{self.type_list}>' + ''.join([f'<li>{entry}</li>'
                for entry in lst]) + f'</{self.type_list}>')


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList()
html = render(lst)
print(html)
