from array.unique_characters import check_unique_characters, check_unique_characters_using_set


def test_check_unique_characters():
    assert(check_unique_characters(''), True)
    assert(check_unique_characters('goo'), False)
    assert(check_unique_characters('abcdefg'), True)
    assert(check_unique_characters('abcde'), True)
    assert(check_unique_characters('aabcde'), False)


def test_check_unique_characters_using_set():
    assert(check_unique_characters_using_set(''), True)
    assert(check_unique_characters_using_set('goo'), False)
    assert(check_unique_characters_using_set('abcdefg'), True)
    assert(check_unique_characters_using_set('abcde'), True)
    assert(check_unique_characters_using_set('aabcde'), False)