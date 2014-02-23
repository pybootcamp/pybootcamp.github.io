#!/usr/bin/env python
"""Concatenate files given on the command line."""

import sys


def print_file(path):
    """Print the contents of the file at the specified path."""
    for line in open(path, 'U'):
        print line.rstrip()


def cat():
    """Concatenate files given as command-line arguments."""
    # Check argument size
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: cat.py file1 file2 ..." 
        sys.exit(1)

    # Get the list of files, which does not include sys.argv[0]
    file_paths = sys.argv[1:]
    for path in file_paths:    
        print_file(path)


if __name__ == "__main__":
    cat()
