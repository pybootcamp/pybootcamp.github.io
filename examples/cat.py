"""Concatenate files."""

import sys

# Check argument size
if len(sys.argv) < 2:
    print >> sys.stderr, "Usage: cat.py file1 file2..." 

# Get the list of files, which does not include sys.argv[0].
file_paths = sys.argv[1:]
for path in file_paths:
    for line in open(path, 'U'):
        print line.rstrip()
