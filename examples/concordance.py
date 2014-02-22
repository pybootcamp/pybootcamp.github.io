"""Example concordance program."""

import sys
import re
import argparse

from collections import Counter, defaultdict


class Concordance(object):
    """A concordance for a text, tracking word frequency and occuring lines.

    >>> c = Concordance("pp_ch1.txt")
    >>> c.lookup("wife")
    ('wife', 4, ['of a good fortune, must be in want of a wife.', '"Do you not want to know who has taken it?" cried his wife impatiently.', '"My dear Mr. Bennet," replied his wife, "how can you be so tiresome! You', 'been insufficient to make his wife understand his character. _Her_ mind'])
    """

    def __init__(self, file_path):
        """Populate the concordance using the text in file_path."""
        self.counter = Counter()
        self.index = defaultdict(list)
        with open(file_path) as f:
            for line in f:
                line = line.strip()
                tokens = set()
                for token in tokenize(line):
                    self.counter[token] += 1
                    if token not in tokens:
                        self.index[token].append(line)
                        tokens.add(token)

    def lookup(self, word):
        """Get the lookup results for the word passed in.

        Raises a ConcordanceWordNotFoundError if the word is not found."""
        clean_word = clean_token(word)
        if clean_word in self.index:
            return clean_word, self.counter[clean_word], self.index[clean_word]
        else:
            raise ConcordanceWordNotFoundError("Couldn't find word {!r}.".format(clean_word))


def main():
    """Parse command line arguments and call the input loop"""
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Build and query a concordance of the specified file.")
    parser.add_argument("file", help="file to build a concordance from")
    args = parser.parse_args()

    # Make a concordance from the file
    try:
        concord = Concordance(args.file)
    # We'll get an IOError if the file cannot be opened
    except IOError:
        print >> sys.stderr, "Couldn't open the input file {!r}.".format(sys.argv[1])
        sys.exit(1)

    # Take input from the user. If the user enters a blank line or interrupts, exit.
    print 'Enter a word to look it up in the concordance.'
    print 'Enter a blank line to exit.'
    while True:
        # Get user input
        try:
            user_input = raw_input('> ')
        except KeyboardInterrupt:
            break
        # If the user entered something, look it up. Otherwise, exit
        if user_input:
            try:
                word, freq, contexts = concord.lookup(user_input)
                print "{} ({})".format(word, freq)
                for line in contexts:
                    print line
                print
            except ConcordanceWordNotFoundError:
                print "The word {!r} was not found.".format(user_input)
                print
        else:
            break

    # Exit if we're out of the loop.
    print 'Exiting...'
    sys.exit()


class ConcordanceWordNotFoundError(IOError):
    """A requested word was not found."""
    pass


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
