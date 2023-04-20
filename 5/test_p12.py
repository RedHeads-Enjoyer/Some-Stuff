from p12 import bucketsort


def test_bucketsort():
    assert bucketsort([1, 2, 3]) == [1, 2, 3]
    assert bucketsort([1, 3, 2]) == [1, 2, 3]
    assert bucketsort([2, 1, 3]) == [1, 2, 3]
    assert bucketsort([2, 3, 1]) == [1, 2, 3]
    assert bucketsort([3, 1, 2]) == [1, 2, 3]
    assert bucketsort([3, 2, 1]) == [1, 2, 3]
    assert bucketsort([1]) == [1]
    assert bucketsort([]) == []
