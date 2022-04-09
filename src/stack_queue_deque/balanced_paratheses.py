from collections import deque


def is_balanced_parenthesis(input_string: str) -> bool:
    """
    Given a string of opening and closing parentheses, check whether it’s balanced.
    We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
    As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
    For example ‘([])’ is balanced but ‘([)]’ is not.
    You can assume the input string has no spaces.
    :param input_string:
    :return:
    """
    parenthesis_deque = deque()
    is_balanced = True
    parenthesis_start = {']': '[', ')': '(', '}': '{'}
    for char in input_string:
        if char in ['[', '{', '(']:
            parenthesis_deque.append(char)
        elif char in [')', '}', ']']:
            if parenthesis_deque.pop() != parenthesis_start[char]:
                is_balanced = False
                break
    if input_string and len(parenthesis_deque) != 0:
        is_balanced = False
    return is_balanced
