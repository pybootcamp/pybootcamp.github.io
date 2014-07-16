#!/usr/bin/env python
"""Average the presidential approval ratings data year-by-year."""

import sys
import csv
from collections import defaultdict


def mean(nums):
    """Compute the mean of a series of numbers."""
    return sum(nums) / float(len(nums))


def median(nums):
    """Compute the median of a series of numbers."""
    # If odd, just get the middle index
    if len(nums) % 2:
        # Use int division to round it downward to get the middle
        # index
        middle = len(nums) / 2
        return nums[middle]
    else:
        # Average the two middle points. These will be len / 2 and the
        # preceding item.
        middle2 = len(nums) / 2
        middle1 = middle2 - 1
        return mean((nums[middle1], nums[middle2]))


def main():
    """Parse arguments and process the data."""
    in_file = open(sys.argv[1], 'U')
    out_path = sys.argv[2]
    reader = csv.reader(in_file)
    # Skip over the header line
    _ = next(reader)
    # Process each row
    ratings = defaultdict(list)
    for row in reader:
        # Ignore the first column, id
        _, year, rating = row
        # Trim the quarter out from the year by turning it into a
        # number and then rounding into an int.
        year = int(float(year))
        if rating != "NA":
            ratings[year].append(int(rating))

    with open(out_path, 'wb') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['year', 'mean', 'median'])
        for year in sorted(ratings):
            year_ratings = ratings[year]
            writer.writerow((year, mean(year_ratings), median(year_ratings)))


if __name__ == "__main__":
    main()
