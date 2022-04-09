from array.sentence_reversal import get_sentence_reversed


def test_get_sentence_reversed():
    assert(get_sentence_reversed("This is the best") == "best the is This")
    assert(get_sentence_reversed("    space before") == "before space")
    assert(get_sentence_reversed("space after     ") == "after space")
    assert(get_sentence_reversed("Hi John,   are you ready to go?") == "go? to ready you are John, Hi")
    assert(get_sentence_reversed("   Hello John    how are you   ") == "you are how John Hello")
    assert(get_sentence_reversed("1") == "1")
    assert(get_sentence_reversed("") == "")
