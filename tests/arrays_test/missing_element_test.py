from arrays.missing_element import find_missing_element, find_missing_element_using_hash_key


def test_find_missing_element_success():
    assert find_missing_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element([5, 5, 7, 7], [5, 7, 7]) == 5
    assert find_missing_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]) == 6


def test_find_missing_element_using_hash_key_success():
    assert find_missing_element_using_hash_key([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element_using_hash_key([5, 5, 7, 7], [5, 7, 7]) == 5
    assert find_missing_element_using_hash_key([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element_using_hash_key([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]) == 6