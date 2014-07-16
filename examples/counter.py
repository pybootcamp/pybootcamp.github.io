"""Implement a simple counter class."""


class Counter(object):
    """Simulate a simple hand counter."""

    def __init__(self):
        """Initialize a counter to zero."""
        self.count = 0

    def __str__(self):
        """Return a string of the count."""
        return str(self.count)

    def __repr__(self):
        """Return a machine-readable string of the count."""
        return "<Counter: {}>".format(self.count)

    def increment(self, amount):
        """Increment the counter."""
        self.count += amount

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
