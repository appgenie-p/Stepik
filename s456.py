from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self) -> int:
        ...

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        self._id = id(self)

    def get_pk(self):
        return self._id
