

def check_unique_characters(input_string: str) -> bool:
    """
    Given a string,determine if it comprises all unique characters.
    For example, the string 'abcde' has all unique characters and should return True.
    The string 'aabcde' contains duplicate characters and should return false.
    :param input_string:
    :return:
    """
    read_chars = {}
    is_unique = True
    for char in input_string:
        if char in read_chars:
            is_unique = False
            break
        else:
            read_chars[char] = 1
    return is_unique


def check_unique_characters_using_set(input_string: str) -> bool:
    """
    Check unique letters using set
    :param input_string:
    :return:
    """
    return len(set(input_string)) == len(input_string)
