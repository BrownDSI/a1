from algorithms.bubblesort import bubble_sort
from algorithms.mergesort import merge_sort

def sorting_tests(sort_fn):
    """A suite of tests to test the correctness of a sorting function sort_fn
    pytest --pyargs algorithms
    """
    assert sort_fn([100]) == [100]
    assert sort_fn([100, -1]) == [-1, 100]
    assert sort_fn([1, 4, 3, 2, 5]) == [1, 2, 3, 4, 5]
    # TASK 1 HERE


def test_sorted():
    sorting_tests(sorted)  # This one will pass


def test_mergesort():
    sorting_tests(merge_sort)


def test_bubblesort():
    sorting_tests(bubble_sort)
