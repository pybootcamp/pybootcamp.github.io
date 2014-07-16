---
layout: bare
title: Classes
---
Use numbered headers: true

<h1>Contents</h1>
* TOC
{:toc}

# When to use classes

While Python doesn't force you to use classes, they're useful in a
number of situations:

1. When you want to centralize storage of multiple data
structures. For example, you may want one class to organize data that
might be spread across several different dictionaries.
1. To extend built-in data structures. For example, let's say you want
to keep track of counts of the number of times you've seen different
words in a file, so you have a dictionary with words as keys and
counts as values. You may want to keep track of the sum of all
the values so you know the total count of how many words you've
counted. You can create something that inherits from a dictionary but
adds a wait to count the total.


# Anatomy of a class

For now, let's consider a class whose goal it is to count upwards from
zero and reset the count if requested. This class is contained in
[counter.py](../examples/counter.py).

{% highlight python %}
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
{% endhighlight %}

Usage of this would look like:
{% highlight python %}
>>> c = Counter() # Initialize a new counter
>>> print repr(c)
<Counter: 0>
>>> print c # Same as str(c)
0
>>> c.increment(1)
>>> c
<Counter: 1>
>>> c.increment(2)
>>> c
<Counter: 3>
>>> c.reset()
>>> c
<Counter: 0>
{% endhighlight %}

A few things to note:

1. Unlike many object-oriented languages, there's no formal way to
define public/private methods and members. Informally, underscores are
used: `count` is public, while `_count` is private.
1. Similarly, the use of get/set functions for simple classes is
discouraged.
1. Every method must take `self` as the first argument.
1. The definition `Counter(object)` says that `Counter` inherits from
`object`, which is the standard base type. In order to get Python to
use its "new-style" way of implementing classes, you must always
explicitly tell it which class to inherit from, even if it's the
default one, `object`.
1. Special method names are surrounded by double
underscores. `__init__` is the constructor, `__str__` provides a
"pretty" string representation, and `__repr__` provides a
"machine-readable" string representation.

# Inheritance

When inheriting from another class, you need to specify which class it
is and override whichever methods you want to. You do not have to
override `__init__`, but if you do make sure to explicitly call
the base class's `__init__`.

To see which methods you want to override in a built-in class, take a
look at the [Python data model
documentation](http://docs.python.org/2/reference/datamodel.html).

Here's an example of overriding `__setitem__` to allow a dictionary to
track the sum over all its values. You can download the full example,
[totaldict.py](../examples/totaldict.py).

{% highlight python %}
class TotalDict(dict):
    """Track the total value of all dictionary keys."""

    def __init__(self):
        dict.__init__(self)
        self.total = 0

    def __setitem__(self, key, value):
        prev_value = self[key] if key in self else 0
        dict.__setitem__(self, key, value)
        self.total += value - prev_value
{% endhighlight %}
 
Here's an example of this class in use:
{% highlight python %}
>>> t = TotalDict()
>>> t.total
0
>>> t['a'] = 5
>>> t.total
5
>>> t['a'] = 3
>>> t.total
3
>>> t['b'] = 5
>>> t.total
8
>>> t['a'] = 7
>>> t.total
12
>>> t['a'] = -100
>>> t.total
-95
>>> t.values()
[-100, 5]
>>> sum(t.values())
-95
{% endhighlight %}
