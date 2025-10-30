import string


sentence = "The quick brown fox jumps over the lazy dog"


def is_pangram(sentence):
    return set(string.ascii_lowercase).issubset(sentence.lower())
