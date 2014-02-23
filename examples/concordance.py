#!/usr/bin/env python
"""Example concordance program."""

import sys
import re
import argparse

from collections import Counter, defaultdict


class Concordance(object):
    """A concordance for a text, tracking word frequency and occuring lines."""

    def __init__(self, file_path):
        """Populate the concordance using the text in file_path."""
        self.counter = Counter()
        self.index = defaultdict(list)
        with open(file_path) as f:
            for line in f:
                line = line.rstrip()
                # Count all occurences of each token
                tokens = tokenize(line)
                self.counter.update(tokens)
                # Only add the line once for each unique token in the
                # line. For example, if 'the' appears twice in the
                # line, the line should only appear once in the index
                # for 'the'.
                for token in set(tokens):
                    self.index[token].append(line)

    def lookup(self, word):
        """Return the sanitized version of the word, its frequency, and the line it appears in.

        Raises a ValueError if the word is not in the concordance."""
        clean_word = clean_token(word)
        if clean_word in self.index:
            return clean_word, self.counter[clean_word], self.index[clean_word]
        else:
            raise ValueError("Unknown word: {!r}.".format(clean_word))


def main():
    """Parse command line arguments and call the input loop"""
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Build and query a concordance of the specified file.")
    parser.add_argument("file", help="file to build a concordance from")
    parser.add_argument("word", help="word to print statistics for")
    args = parser.parse_args()

    # Make a concordance from the file
    try:
        concord = Concordance(args.file)
    # We'll get an IOError if the file cannot be opened
    except IOError:
        print >> sys.stderr, "Couldn't open input file {!r}.".format(sys.argv[1])
        sys.exit(1)

    # Look up the word
    try:
        word, freq, contexts = concord.lookup(args.word)
        print "{} ({})".format(word, freq)
        for line in contexts:
            print line
    except ValueError:
        print "The word {!r} was not found.".format(args.word)


def clean_token(token):
    """Return a sanitized version of the token.

    >>> clean_token('she') == clean_token('SHE') == clean_token('ShE')
    True
    """
    return re.sub("[^a-zA-Z']", '', token.lower())


def tokenize(line):
    """Return a sequence representing a tokenized version of the line.

    Splits on spaces and then cleans each token up.

    >>> tokenize('This is a "bunch" of text.')
    ['this', 'is', 'a', 'bunch', 'of', 'text']
    """
    return [clean_token(token) for token in line.split()]


if __name__ == "__main__":
    main()
