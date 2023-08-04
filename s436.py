from typing import Any, Callable, Dict, Optional

F = Callable[..., Any]


class Router:
    app: Dict[str, F] = {}

    @classmethod
    def get(cls, path: str) -> Optional[F]:
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path: str, func: F) -> None:
        cls.app[path] = func


# @Callback('/', Router)
# def index():
#     return '<h1>Главная</h1>'


# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)
