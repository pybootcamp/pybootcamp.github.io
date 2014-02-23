"""Provides the TotalDict class."""


class TotalDict(dict):
    """Track the total value of all dictionary keys."""

    def __init__(self):
        dict.__init__(self)
        self.total = 0

    def __setitem__(self, key, value):
        prev_value = self[key] if key in self else 0
        dict.__setitem__(self, key, value)
        self.total += value - prev_value
