from s545 import PrimaryKeyError


def test_PrimaryKeyError_message():
    try:
        raise PrimaryKeyError()
    except PrimaryKeyError as e:
        assert (
            str(e) == "Первичный ключ должен быть целым неотрицательным числом"
        )


def test_PrimaryKeyError_message1():
    err1 = PrimaryKeyError()
    assert (
        str(err1) == "Первичный ключ должен быть целым неотрицательным числом"
    )


def test_PrimaryKeyError_message2():
    e2 = PrimaryKeyError(id="abc")
    assert str(e2) == "Значение первичного ключа id = abc недопустимо"
