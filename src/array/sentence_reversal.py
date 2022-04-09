

def get_sentence_reversed(sentence: str) -> str:
    """
    Given a string of words, reverse all the words.
    For example: 'This is the best' => 'best the is This'

    As part of this exercise you should remove all leading and trailing whitespace.
    '  space here'  and 'space here      ' both become 'here space'

    :param sentence:
    :return:
    """
    # return " ".join(sentence.split()[::-1])  # This also works
    return " ".join(reversed(sentence.split()))
