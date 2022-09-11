import pytest

set_1 = {1, 2, 3, 4, 5}
set_2 = {1}


def IsSet(mySet):
    return isinstance(mySet, set)

def SetsHasIntersection(fist_set, second_set):
    intersetcion = fist_set.intersection(second_set)
    return bool(intersetcion)

def test_one():
    assert IsSet(set_1) == True

def test_two():
        assert SetsHasIntersection(set_1, set_2) == True

def test_three():
    try:
        assert set_1.remove('a')
    except TypeError:
        pass


