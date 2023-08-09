import pytest

from s457 import Stack, StackObj


def test_stackobj_data_setting():
    stack_object = StackObj("some data")
    assert stack_object._data == "some data"


def test_stackobj_next_setting():
    stack_object = StackObj("some data")
    stack_object.next = StackObj("some data")
    assert stack_object.next._data == "some data"


@pytest.fixture
def so():
    return [StackObj("some data") for _ in range(3)]


@pytest.fixture
def s():
    return Stack()


def test_stack_push_back_first(s, so):
    s.push_back(so[0])
    assert s._top == so[0]


def test_stack_push_back_second(s, so):
    s.push_back(so[0])
    s.push_back(so[1])
    assert s._top == so[0]
    assert s._top.next == so[1]


def test_stack_push_back_third(s, so):
    s.push_back(so[0])
    s.push_back(so[1])
    s.push_back(so[2])
    assert s._top == so[0]
    assert s._top.next == so[1]
    assert s._top.next.next == so[2]

def test_stack_pop_back_from_one(s, so):
    s.push_back(so[0])
    assert s.pop_back() == so[0]
    assert s._top == None


def test_stack_pop_back_from_two(s, so):
    s.push_back(so[0])
    s.push_back(so[1])
    assert s.pop_back() == so[1]
    assert s._top.next == None