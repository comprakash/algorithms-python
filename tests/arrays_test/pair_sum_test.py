from arrays.pair_sum import get_pair_sum


def test_pair_sum_found():
    assert not get_pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10).difference(
        {(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (-1, 11)})
    assert not get_pair_sum([1, 2, 3, 1], 3).difference({(1, 2)})
    assert not get_pair_sum([1, 3, 2, 2], 4).difference({(1, 3), (2, 2)})


def test_pair_sum_not_found():
    assert not get_pair_sum([1, 2, 3, 8], 7)
    assert not get_pair_sum([0, 1, 2, -1], 4)
