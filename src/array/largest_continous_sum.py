from typing import List


def find_largest_continuous_sum(number_array: List[int]) -> int:
    """
    Given an array of integers (positive and negative) find the largest continuous sum.
    :param number_array:
    :return:
    """
    if len(number_array) > 0:
        max_sum = current_sum = number_array[0]
        for number in number_array[1:]:
            current_sum = max(current_sum + number, number)
            max_sum = max(current_sum, max_sum)
        return max_sum
    else:
        return 0


def find_largest_continuous_sum_using_window(number_array: List[int]) -> int:
    """
    Given an array of integers (positive and negative) find the largest continuous sum.
    :param number_array:
    :return:
    """
    max_sum = 0
    for start_position in range(len(number_array)):
        for x in range(len(number_array) - start_position):
            current_sum = sum(number_array[start_position:start_position+x+1])
            max_sum = max(current_sum, max_sum) if max_sum else current_sum
    return max_sum
