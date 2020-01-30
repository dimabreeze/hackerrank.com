from array_manipulation import arrayManipulation


def test_sample_input_0():
    assert arrayManipulation(10, [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1]]) == 10


def test_sample_input_1():
    assert arrayManipulation(5, [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100]]) == 200


def test_sample_input_2():
    assert arrayManipulation(10, [
        [2, 6, 8],
        [3, 5, 7],
        [1, 8, 1],
        [5, 9, 15]]) == 31
