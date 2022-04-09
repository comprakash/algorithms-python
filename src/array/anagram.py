import re
from collections import defaultdict


def check_if_anagram_using_sort(input1: str, input2: str) -> bool:
    cleaned_input1 = "".join(re.findall("[a-z0-9]+", input1.lower()))
    cleaned_input2 = "".join([c for c in input2.lower() if c.isalnum()])
    return sorted(cleaned_input1) == sorted(cleaned_input2)


def check_if_anagram(input1: str, input2: str) -> bool:
    """
    Given two strings, check to see if they are anagrams.
    An anagram is when the two strings can be written using the exact same letters.
    So you can just rearrange the letters to get a different phrase or word.
    For example:
    "public relations" is an anagram of "crap built on lies."
    "clint eastwood" is an anagram of "old west action"
    :param input1: First Input Sentence
    :param input2: Second Input Sentence
    :return: bool: Whether the strings are Anagrams or not
    """
    cleaned_input1 = [letter for letter in input1.lower() if letter.isalnum()]
    cleaned_input2 = [letter for letter in input2.lower() if letter.isalnum()]
    is_anagram = False
    letter_count = defaultdict(int)
    if len(cleaned_input1) == len(cleaned_input2):
        for letter in cleaned_input1:
            letter_count[letter] += 1
        for letter in cleaned_input2:
            letter_count[letter] -= 1
        for key in letter_count:
            if letter_count[key] != 0:
                break
        is_anagram = True
    return is_anagram


