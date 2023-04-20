import pytest

from p21 import binary_search


@pytest.fixture
def arr():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_binary_search(arr):
    assert binary_search(arr, 6) == 5


def test_binary_search(arr):
    assert binary_search(arr, 10) == -1


# @pytest.mark.parametrize('val, index', [
#     (1, 0),
#     (2, 1),
#     (6, 5),
#     (10, -1)
# ])

# def binary_search(arr, val, index):
#     assert binary_search(arr, val) == index


# pytest
