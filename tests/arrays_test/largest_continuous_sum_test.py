from arrays.largest_continous_sum import find_largest_continuous_sum, find_largest_continuous_sum_using_window


def test_largest_continuous_sum():
    assert (find_largest_continuous_sum([1, 2, -1, 3, 4, -1]) == 9)
    assert (find_largest_continuous_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]) == 29)
    assert (find_largest_continuous_sum([1, 2, -1, 3, 4, 10, -1, 10, -10, -1]) == 28)
    assert (find_largest_continuous_sum([-1, 1]) == 1)
    assert (find_largest_continuous_sum([-2, -3, -1, -5]) == -1)
    assert (find_largest_continuous_sum([]) == 0)


def test_largest_continuous_sum_using_window():
    assert (find_largest_continuous_sum_using_window([1, 2, -1, 3, 4, -1]) == 9)
    assert (find_largest_continuous_sum_using_window([1, 2, -1, 3, 4, 10, 10, -10, -1]) == 29)
    assert (find_largest_continuous_sum_using_window([1, 2, -1, 3, 4, 10, -1, 10, -10, -1]) == 28)
    assert (find_largest_continuous_sum_using_window([-1, 1]) == 1)
    assert (find_largest_continuous_sum_using_window([-2, -3, -1, -5]) == -1)
    assert (find_largest_continuous_sum_using_window([]) == 0)
