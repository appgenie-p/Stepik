from collections import defaultdict
from typing import Any, Callable, Dict, Optional, Type

F = Callable[..., Any]


class Router:
    app: Dict[str, F] = defaultdict(F)

    @classmethod
    def get(cls, path: str) -> Optional[F]:
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path: str, func: F) -> None:
        cls.app[path] = func


class Callback:
    def __init__(self, path: str, router: Type[Router]) -> None:
        self.path = path
        self.router = router

    def __call__(self, func: F) -> F:
        self.router.add_callback(self.path, func)
        return func
