#!/usr/bin/env python
"""Create a wordlist from tokenized text."""

import sys
from collections import Counter


def make_wordlist():
    """Make a wordlist from the first command-line argument."""
    filename = sys.argv[1]

    counter = Counter()
    for line in open(filename, 'U'):
        for word in line.split():
            counter[word] += 1

    for word, count in counter.most_common():
        print count, word


if __name__ == "__main__":
    make_wordlist()
