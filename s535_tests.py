import pytest

from s535 import Test, TestAnsDigit


def test_test_class_creation():
    assert Test("test")


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
    assert TestAnsDigit("testtesttest", 1, 1)


def test_Test_Ans_Digit_class_err1():
    with pytest.raises(ValueError):
        TestAnsDigit("testtesttest", 1, -1)


def test_Test_Ans_Digit_class_err():
    with pytest.raises(ValueError):
        TestAnsDigit("testtesttest", "1", 1)
