from typing import Any, Mapping

Request = Mapping[str, Any]


class RetriveMixin:
    def get(self, request: Request) -> str:
        return "GET: " + request.get("url", "")


class CreateMixin:
    def post(self, request: Request) -> str:
        return "POST: " + request.get("url", "")


class UpdateMixin:
    def put(self, request: Request) -> str:
        return "PUT: " + request.get("url", "")


class GeneralView:
    allowed_methods = ("GET", "POST", "PUT", "DELETE")

    def render_request(self, request: Request) -> str:
        self._request = request
        self._if_request_method_not_allowed_raise_type_error()
        return self._create_response()

    def _create_response(self):
        self.request_method = self._request.get("method", "").lower()
        return getattr(self, self.request_method)(self._request)

    def _if_request_method_not_allowed_raise_type_error(self):
        if self._request.get("method") not in self.allowed_methods:
            raise TypeError(f"Метод {self._request.get('method')} не разрешен.")


class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ("GET", "PUT")
