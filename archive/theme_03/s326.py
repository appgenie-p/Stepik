from typing import List


class TypeList:
    def __set_name__(self, obj, name):
        self.name = '_' + name

    def __set__(self, obj, val):
        if val not in ('ul', 'ol'):
            val = 'ul'
        setattr(obj, self.name, val)

    def __get__(self, obj, type=None):
        return getattr(obj, self.name)


class RenderList:
    def __init__(self, type_list: str = 'ul'):
        self.type_list = type_list

    def __call__(self, lst: List[str]) -> str:
        return ('\n'.join([f'<{self.type_list}>', *(f'<li>{entry}</li>'
                for entry in lst), f'</{self.type_list}>']))


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
