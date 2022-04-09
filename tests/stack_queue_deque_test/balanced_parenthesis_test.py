from stack_queue_deque.balanced_paratheses import is_balanced_parenthesis


def test_is_balanced_parenthesis():
    assert is_balanced_parenthesis("([])")
    assert is_balanced_parenthesis("[]")
    assert is_balanced_parenthesis("[awesome]")
    assert is_balanced_parenthesis("[{{{(())}}}]((()))")
    assert is_balanced_parenthesis("[a{b{c{d(e(f)g)h}i}j}k](((12345)))")
    assert is_balanced_parenthesis("[](){([[[]]])}")
    assert not is_balanced_parenthesis("[](){([[[]]])}(")
    assert not is_balanced_parenthesis("[[[]])]")
    assert not is_balanced_parenthesis("[[a[]])b]")
    assert not is_balanced_parenthesis("()(){]}")
