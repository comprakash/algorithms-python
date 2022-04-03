from typing import List, Tuple, Set


def get_pair_sum(number_array: List[int], sum_of_numbers: int) -> Set[Tuple[int, int]]:
    """
    Given an integer array, output all the unique pairs that sum up to a specific value k.
    So the input: pair_sum([1,3,2,2],4)
    would return 2 pairs: (1,3) and (2,2)
    :param number_array: Input array of numbers
    :param sum_of_numbers: Sum of numbers
    :return: Pairs whole sum is equal to the input sum_of_numbers
    """
    pairs = set()
    if len(number_array) >= 2:
        seen = set()
        for number in number_array:
            target = sum_of_numbers - number
            if target not in seen:
                seen.add(number)
            else:
                pairs.add((min(number, target), max(number, target)))
    return pairs
