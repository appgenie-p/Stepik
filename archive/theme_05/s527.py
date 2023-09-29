from numbers import Real


def get_loss(w1: Real, w2: Real, w3: Real, w4: Real) -> Real:
    try:
        mid_res = 10 * w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        return mid_res - 5 * w2 * w3 + w4
