class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return [self.render(digit) for digit in func(*args, **kwargs).split()]

        return wrapper


class RenderDigit:
    def __call__(self, string: str):
        try:
            return int(string)
        except ValueError:
            return None


render = RenderDigit()


# @InputValues(render)
def input_dg(string):
    return string


r = InputValues(RenderDigit())(input_dg)("123 rrr 555")

# res = input_dg("123 rrr 555")
print(r)

# assert render("123") == 123, 'не целое число)'
# assert render("45.54") is None, 'не (не целое число)'
# assert render("-56") == -56, 'не целое число)'
# assert render("12fg") is None, 'не (не целое число)'
# assert render("abc") is None, 'не (не целое число)'
