---
layout: bare
title: Odds and Ends
---

# Contents
{:.no_toc}
1. TOC
{:toc}

# Argument parsing using argparse

Parsing `sys.argv` yourself can be quite a pain. If your program takes
more than one or two fixed arguments, it can be very handy to use
[argparse](http://docs.python.org/2.7/library/argparse.html), which
does all the hard work for you. Take a look at the [concordance
example](../examples/concordance.py) to see this in use.

# Collections

Many simple tasks like constructing dictionaries with default values
and keeping track of counts are made easier by the
[defaultdict](http://docs.python.org/2.7/library/collections.html#collections.defaultdict)
and
[Counter](http://docs.python.org/2.7/library/collections.html#collections.Counter)
classes. Take a look at the [documentation on
collections](http://docs.python.org/2.7/library/collections.html) for
an overview.

# Scientific computing

Check out [NumPy](http://www.numpy.org/) and
[SciPy](http://www.scipy.org/). NumPy provides an array type, linear
algebra functions, Fourier transform, and a number of other handy
numeric features. SciPy provides routines for optimization and
integration, reading MATLAB structures, and a number of other useful
things.
