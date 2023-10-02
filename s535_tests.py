import pytest
from _pytest.monkeypatch import MonkeyPatch

from s535 import Test, TestAnsDigit, main


def test_test_creation_err_with_wrong_descr_size():
    descr_min = "a" * 9
    descr_max = "a" * 11000
    with pytest.raises(ValueError):
        Test(descr_min)
    with pytest.raises(ValueError):
        Test(descr_max)


def test_test_run_method_definition_in_child_class():
    class ChildTest(Test):
        pass

    with pytest.raises(NotImplementedError):
        ChildTest("testtesttest").run()


def test_Test_Ans_Digit_class():
    test = TestAnsDigit("testtesttest", 1, 1)
    assert test.name == "testtesttest"
    assert test.ans_digit == 1
    assert test.max_error_digit == 1


def test_Test_Ans_Digit_class_err1():
    with pytest.raises(ValueError):
        TestAnsDigit("testtesttest", 1, -1)


def test_Test_Ans_Digit_class_err():
    with pytest.raises(ValueError):
        TestAnsDigit("testtesttest", "1", 1)
    with pytest.raises(ValueError):
        TestAnsDigit("testtesttest", True, 1)


@pytest.fixture
def user_input(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda: "5.05")


def test_testansdigit_run_valid_answer(monkeypatch: MonkeyPatch):
    test = TestAnsDigit("Test description", 5.0, 0.1)
    monkeypatch.setattr("builtins.input", lambda: "5.05")
    assert test.run() == True


def test_testansdigit_run_envalid_answer(monkeypatch: MonkeyPatch):
    test = TestAnsDigit("Test description", 5.0, 0.1)
    monkeypatch.setattr("builtins.input", lambda: "5.2")
    assert test.run() == False


def test_1():
    try:
        test = Test("descr")
    except ValueError:
        assert True
    else:
        assert False, (
            "не сгенерировалось исключение ValueError при вызове "
            "инициализатора класса Test с неверным набором аргументов"
        )


def test_2():
    try:
        test = Test("descr ghgfhgjg ghjghjg")
        test.run()
    except NotImplementedError:
        assert True
    else:
        assert False

    assert issubclass(TestAnsDigit, Test)

    t = TestAnsDigit("ffhgfh fghfghfghfggfhfghfh", 1)
    t = TestAnsDigit("ffhgfh fghfghfghfggfhfghfh", 1, 0.5)

    try:
        t = TestAnsDigit("ffhgfh fghfghfghfggfhfghfh", 1, -0.5)
    except ValueError:
        assert True
    else:
        assert False


def test_main_valid(monkeypatch: MonkeyPatch):
    input_1 = "Какое значение получим, при выполнении команды int(5.7)? | 5"
    input_2 = "2"
    inputs = iter([input_1, input_2])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    assert main() is False


def test_main_invalid(monkeypatch: MonkeyPatch):
    input_1 = "Как | 5"
    input_2 = "2"
    inputs = iter([input_1, input_2])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    with pytest.raises(ValueError):
        main()