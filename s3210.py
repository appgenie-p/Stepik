class InputValues:
    def __init__(self, render):
        """render - функция или объект для преобразования данных из строк в
        другой тип данных
        """
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            pass
        return wrapper


class RenderDigit:
    def __call__(self, string: str):
        try:
            return int(string)
        except ValueError:
            return None


render = RenderDigit()


@InputValues(render)
def input_dg():
    return input()


res = input_dg()
print(res)

# assert render("123") == 123, 'не целое число)'
# assert render("45.54") is None, 'не (не целое число)'
# assert render("-56") == -56, 'не целое число)'
# assert render("12fg") is None, 'не (не целое число)'
# assert render("abc") is None, 'не (не целое число)'
