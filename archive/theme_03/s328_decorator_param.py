class Handler:
    def __init__(self, methods=('GET',)) -> None:
        self.methods = methods

    def get(self, func, request):
        return f"GET: {func(request)}"

    def post(self, func, request):
        return f"POST: {func(request)}"

    def __call__(self, func):
        def wrapper(request):
            method = request.get('method', 'GET')
            if method not in self.methods:
                return
            method_lower = method.lower()
            return self.__getattribute__(method_lower)(func, request)
        return wrapper


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"

assert contact({"method": "POST", "url": "contact.html"}) == "POST: Сергей Балакирев"

assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"

assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

@Handler(methods=('POST'))
def index(request):
    return "index"

assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"


