from collections import defaultdict
from typing import List


def find_missing_element(number_array_1: List[int], number_array_2: List[int]) -> int:
    """
    Consider an array of non-negative integers.
    A second array is formed by shuffling the elements of the first array and deleting a random element.
    Given these two arrays, find which element is missing in the second array.

    Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
    Input: finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    Output: 5 is the missing number

    Uses XOR concept

    :param number_array_1:
    :param number_array_2:
    :return:
    """
    result = 0
    for number in number_array_1 + number_array_2:
        result ^= number
    return result


def find_missing_element_using_hash_key(number_array_1: List[int], number_array_2: List[int]) -> int:
    """
    find_missing_element using default dict (Hash Key)
    :param number_array_1:
    :param number_array_2:
    :return:
    """
    number_count = defaultdict(int)
    for number in number_array_2:
        number_count[number] += 1
    for number in number_array_1:
        if number_count[number] == 0:
            return number
        else:
            number_count[number] -= 1
