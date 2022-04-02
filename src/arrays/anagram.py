import re


def check_if_anagram(input1: str, input2: str) -> bool:
    cleaned_input1 = "".join(re.findall("[a-z0-9]+", input1.lower()))
    cleaned_input2 = "".join([c for c in input2.lower() if c.isalnum()])
    return sorted(cleaned_input1) == sorted(cleaned_input2)


