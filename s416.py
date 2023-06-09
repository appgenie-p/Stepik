"""This module contains classes for handling generic views."""

from abc import abstractmethod
from typing import List, Tuple, Union

Methods = Union[List[str], Tuple[str, ...]]


class GenericView:
    """GenericView: A class for handling generic views."""

    def __init__(self, methods: Methods = ('GET',)):
        self.methods = methods

    @abstractmethod
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    """DetailView: A class for handling detail views."""

    def render_request(self, request: dict, method: str) -> str:
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

        current_method = getattr(self, method.lower())
        return current_method(request)

    def get(self, request: dict) -> str:
        return f"url: {request['url']}"


dv = DetailView(('GET', 'POST'))
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)
