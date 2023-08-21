from abc import ABC, abstractmethod
from typing import Any, Dict, Mapping

Request = Mapping[str, Any]


class Strategy(ABC):
    @abstractmethod
    def execute(self, request: Request) -> str:
        ...


class RetriveMixin(Strategy):
    def execute(self, request: Request) -> str:
        return "GET: " + request.get("url", "")


class CreateMixin(Strategy):
    def execute(self, request: Request) -> str:
        return "POST: " + request.get("url", "")


class UpdateMixin(Strategy):
    def execute(self, request: Request) -> str:
        return "PUT: " + request.get("url", "")


class GeneralView:
    allowed_methods = ("GET", "POST", "PUT", "DELETE")

    def __init__(self) -> None:
        self.strategies: Dict[str, Strategy] = {
            "GET": RetriveMixin(),
            "POST": CreateMixin(),
            "PUT": UpdateMixin(),
        }

    def render_request(self, request: Request) -> str:
        self._request = request
        self._request_method = self._request.get("method", "")
        self._if_request_method_not_allowed_raise_type_error()
        strategy = self.strategies.get(self._request_method)
        if not strategy:
            raise NotImplementedError(
                f"Стратегия {self._request_method} не определена."
            )
        return strategy.execute(self._request)

    def _if_request_method_not_allowed_raise_type_error(self):
        if self._request_method not in self.allowed_methods:
            raise TypeError(f"Метод {self._request.get('method')} не разрешен.")


class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ("GET", "PUT")
