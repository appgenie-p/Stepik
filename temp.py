try:
    x, y = map(float, input().split())
    d = x / y
except ArithmeticError:
    print('ArithmeticError')
except ZeroDivisionError:
    print('ZeroDivisionError')
