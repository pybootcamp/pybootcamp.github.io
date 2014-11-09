---
layout: bare
title: Exercises
---

# Contents
{:.no_toc}
1. TOC
{:toc}

# Data to work with

We'll work with a data set that is a count of how often each word
appeared in a 1 million-word corpus of American English text called
the Brown corpus. Download [this
wordlist](../examples/brown_wordlist.txt). Each line has a frequency
and a word separated by a space, so you can extract them by calling
`split` on the line after you call `rstrip`. Each word appears only
once.

You're going to write programs to produce counts of various things in
this corpus. Python provides some useful collections classes to make
counting easier, such as `Counter` and `defaultdict`. We aren't going
to use those yet since they make the job too easy.

# Data processing

Make a separate file for each of the following problems. You'll want
each solution to build on the previous one, so you'll probably want to
copy/paste code across them. Each file should be runnable on its own
and take a single command line argument, the filename of the wordlist.

## Basic reading

First, write a program that takes the input file and creates a
dictionary where the keys are the words and the values are the
frequencies. As a sanity check, print out 10 entries from the
dictionary (keys and values) to make sure you've got it right.

## Sorting

You may want to be able to find items more easily. Building on the
previous program, instead of printing out keys and values in the
(arbitrary) dictionary order, sort the keys alphabetically using the
`sorted` function and then print each word and its frequency in the
sorted order.

## Character counts

Let's say we instead want to count the number of times each character
appears. For example, if 'he' has a frequency of 9548, count that we
saw 'h' 9548 times and 'e' 9548 times. Print out the frequency of each
letter computed in this fashion over the wordlist.

## Solution

For an example solution, look at
[read_wordlist.py](../examples/read_wordlist.py).


# Extensions

If you've gotten to the end easily, look at how you might clean up
your solutions or organize them differently. Some suggestions:

- Make some general functions that do things you did repeatedly.
- Figure out how to sort a dictionary by value so you can print out
  the letter frequencies in order of most frequent to least.
- Take a look at [Python
collections](http://docs.python.org/2/library/collections.html) and
reimplement these exercises. Isn't that easier?

# Another challenge

If you've made it this far, nice work!

Now it's time to make your own wordlist. Assume you have a file that's
a [tokenized version of chapters 1-2 of _Pride and
Prejudice_](../examples/pp_ch1-2_tokenized.txt). Write a program that
will produce a wordlist from it. The output should look like [this
wordlist](../examples/pp_ch1-2_wordlist.txt).

For an example solution, look at
[make_wordlist.py](../examples/make_wordlist.py).
