import pytest

tuple_1 = (1, '2', False)
tuple_2 = ('a', 'b')

print(tuple_1 * tuple_2)

def IsTuple(myTuple):
    return isinstance(myTuple, tuple)

def test_one():
    assert IsTuple(tuple_1) == True

def test_two():
    assert  tuple_1.__contains__(1)

def test_three():
    try:
        assert tuple_one * tuple_2
    except TypeError:
        pass
