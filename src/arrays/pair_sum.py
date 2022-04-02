from typing import List, Tuple, Set


def get_pair_sum(number_array: List[int], sum_of_numbers: int) -> Set[Tuple[int, int]]:
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
