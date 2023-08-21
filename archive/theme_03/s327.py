from collections.abc import Callable
from typing import Dict


class HandlerGET:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def get(self, func: Callable, request, *args, **kwargs):
        return_str = func(request)
        method = request.get("method", "GET")
        if method == "GET":
            return f"GET: {return_str}"
        return None

    def __call__(self, request: Dict[str, str]) -> str:
        return self.get(self.func, request)


@HandlerGET
def index(request):
    return "главная страница сайта"


res = index({"method": "GET"})
assert (
    res == "GET: главная страница сайта"
), "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert (
    res == "GET: главная страница сайта"
), "декорированная функция вернула неверные данные"
