from collections import defaultdict


def compress_repeating_letters(input_string: str) -> str:
    """
    Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
    For this problem, you can falsely "compress" strings of single or double letters.
    For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
    The function should also be case-sensitive, so that a string 'AAAaaa' returns 'A3a3'.
    :param input_string:
    :return:
    """
    letter_count = defaultdict(int)
    for i, char in enumerate(input_string):
        letter_count[char] += 1
    compressed_string = ""
    for key, value in letter_count.items():
        compressed_string += key + str(value)
    return compressed_string
