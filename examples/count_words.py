#!/usr/bin/env python
"""Create a wordlist from multiple files."""

import sys
from collections import Counter


def gen_tokens(filenames):
    """Generate tokens from each file."""
    for filename in filenames:
        input_file = open(filename, "U")
        for line in input_file:
            for token in line.split():
                yield token


def count_tokens(tokens):
    """Return a counter for the given tokens."""
    return Counter(tokens)


def count_words():
    """Parse arguments and do the work."""
    filenames = sys.argv[1:]
    token_generator = gen_tokens(filenames)
    word_freqs = count_tokens(token_generator)
    for word, count in word_freqs.most_common(10):
        print count, word


if __name__ == "__main__":
    count_words()
