from array.string_compression import compress_repeating_letters


def test_compress_repeating_letters():
    assert(compress_repeating_letters("") == "")
    assert(compress_repeating_letters("AABBCC") == "A2B2C2")
    assert(compress_repeating_letters("AAABCCDDDDD") == "A3B1C2D5")
    assert(compress_repeating_letters("AAAaaa") == "A3a3")
    assert(compress_repeating_letters("AAB") == "A2B1")
    assert(compress_repeating_letters("AAAABBBBCCCCCDDEEEE") == "A4B4C5D2E4")
