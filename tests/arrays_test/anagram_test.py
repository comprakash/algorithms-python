from arrays.anagram import check_if_anagram, check_if_anagram_using_sort


def test_anagram_success():
    assert check_if_anagram("public relations", "crap built on lies!")
    assert check_if_anagram("clint eastwood", "old west action")
    assert check_if_anagram("Mother-in-law", "Woman Hitler")
    assert check_if_anagram("Debit card", "Bad credit")
    assert check_if_anagram("Election results", "Lies – let's recount")
    assert check_if_anagram("A decimal point", "I'm a dot in place")


def test_anagram_failure():
    assert not check_if_anagram("public relations", "crap built on a lies")
    assert not check_if_anagram("clint eastwood", "old west action1")


def test_anagram_using_sort_success():
    assert check_if_anagram_using_sort("public relations", "crap built on lies!")
    assert check_if_anagram_using_sort("clint eastwood", "old west action")
    assert check_if_anagram_using_sort("Mother-in-law", "Woman Hitler")
    assert check_if_anagram_using_sort("Debit card", "Bad credit")
    assert check_if_anagram_using_sort("Election results", "Lies – let's recount")
    assert check_if_anagram_using_sort("A decimal point", "I'm a dot in place")


def test_anagram_using_sort_failure():
    assert not check_if_anagram_using_sort("public relations", "crap built on a lies")
    assert not check_if_anagram_using_sort("clint eastwood", "old west action1")
