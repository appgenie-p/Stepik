class Car:
    # def __init__(self) -> None:
    #     self.__model: str = ''

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, auto_model: str) -> None:
        if isinstance(auto_model, str) and 2 <= len(auto_model) <= 100:
            self.__model = auto_model

    
car = Car()
car.model = 'sss'
print(car.__dict__)
print(dir(car))
print(vars(car))
