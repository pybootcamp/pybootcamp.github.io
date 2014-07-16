---
layout: bare
title: More on Iteration
---
Use numbered headers: true

<h1>Contents</h1>
* TOC
{:toc}

# Comprehensions

## List comprehensions

Very often, we want to build up lists by processing another iterable,
which might be another list or anything else we can loop over. For
example, consider the problem of a text file which we want to split
into individual words and treat as a list. For example, consider the
first paragraph of the first chapter of _Pride and Prejudice_,
with punctuation removed and words in lowercase:

<pre>
it is a truth universally acknowledged that a single man in possession
of a good fortune must be in want of a wife
</pre>

The data comes from a [tokenized version of chapters 1-2 of _Pride and
Prejudice_](../examples/pp_ch1-2_tokenized.txt). We may want to
transform this into a list of the individual words:

{% highlight python %}
['it', 'is', 'a', 'truth', 'universally', 'acknowledged', 'that',
'a', 'single', 'man', 'in', 'possession', 'of', 'a', 'good',
'fortune', 'must', 'be', 'in', 'want', 'of', 'a', 'wife']
{% endhighlight %}

We can imagine a simple way to do this:

{% highlight python %}
in_file = open("pp_ch1-2_tokenized.txt", "U")
words = []
for line in in_file:
    # Split the line into individual words
    tokens = words.split()
    # Add them to the list of words
    words.extend(tokens)
{% endhighlight %}

This is going to be rather slow and inefficient for building larger
lists because `words` will be resized repeatedly.

Instead, we can build a list with a powerful syntactic construct
called a _list comprehension_. Let's first consider the simplest list
comprehension possible, one that just make a copy of a list.

{% highlight python %}
old_list = ['a', 'b', 'c', 'D', 'E', 'F']
new_list = [item for item in old_list]
{% endhighlight %}

`new_list` will contain the exact contents of `old_list`, equivalent
to `new_list = old_list[:]`. The list comprehension is equivalent to
this:

{% highlight python %}
new_list = []
for item in old_list:
    new_list.append(item)
{% endhighlight %}

It's just much cleaner to write and more efficient. Of course, we may
want to do things that are more complicated:

{% highlight python %}
# Convert all items to lowercase
lower_list = [item.lower() for item in old_list]
# Get rid of any item that is 'c'
no_c_list = [item for item in old_list if item != 'c']
# Add 'The letter ' to each item
letter_list = ["The letter " + item for item in old_list]
{% endhighlight %}

Now that we understand the basics, we can return to the original
problem, which requires two loops:

{% highlight python %}
words = [word for line in open("pp_ch1-2_tokenized.txt", "U")
         for word in line.split()]
{% endhighlight %}

The line break in the middle of the comprehension is just for visual
clarity; it doesn't change the meaning of it at all.

## Generators

While the above example is useful, it's rather inefficient because it
creates a huge list of all of the words in memory at once.

If we only look at one word at a time, we can write this in a very
slightly different way to make it more efficient:

{% highlight python %}
gen_words = (word for line in open("pp_ch1-2_tokenized.txt", "U")
             for word in line.split())
{% endhighlight %}

This is what's called a _generator expression_, which means that
rather than creating a list is creates a generator that _yields_ the
same contents. The catch is that you can only iterate over the result
once.

We can also write generator functions. For example, this function
yields Fibonacci numbers:

{% highlight python %}
def fib(n):
    """Generate the first n Fibonacci numbers."""
    f0 = 0
    f1 = 1
    for count in range(n):
        # F0 and F1 are special cases
        if count == 0:
            yield f0
        elif count == 1:
            yield f1
        else:
            result = f0 + f1
            yield result
            f0 = f1
            f1 = result
{% endhighlight %}

As an exercise, you'll rewrite the expression for `gen_words` as a generator function 

## Dictionary comprehensions

In one of the previous exercises, we built a dictionary mapping words
to their frequencies from a file that looked like this:

<pre>
69971 the
36412 of
28853 and
26158 to
23195 a
21337 in
10594 that
10109 is
9815 was
9548 he
</pre>

This can easily be written as a dictionary comprehension:
{% highlight python %}
word_freqs = {line.split()[1]: int(line.split()[0]) for line in in_file}
{% endhighlight %}

It's a little ugly because we can't store the result of calling
`split` anywhere so we have to call it twice. We can also create
dictionaries in a similar fashion using the `dict` constructor, which
will work when given tuples of the format `(key, value)`:

{% highlight python %}
word_freqs = dict((line.split()[1], int(line.split()[0])) for line in in_file)
{% endhighlight %}

Inside the call to `dict` we are actually using a generator
expression.

We can make a modified copy of a dictionary easily using a dictionary
comprehension:

{% highlight python %}
# Make a new dictionary with one added to every frequency
word_freqs2 = {word: freq + 1 for word, freq in word_freqs.iteritems()}
{% endhighlight %}

You'll noticed I used `iteritems` instead of the normal `items`. There
are similar `iterkeys` and `itervalues` methods. Inside a
comprehension, which tries to be as memory-efficient as possible, it's
best to use these iterator forms. That said, you will see no
difference at all between `items` and `iteritems` much of the time.

# Exercises

## Counting words

Your goal is to create a dictionary that maps words to their
frequencies, similar to the contents of the [Brown corpus
wordlist](../examples/brown_wordlist.txt) that we worked with
before.

Your file `count_words.py` will take filenames as command-line
arguments and use a `Counter` (a special kind of dictionary defined
in `collections`) to count their frequencies.

It's easiest to think of this as writing three functions:

1. A main function that gets the arguments from the command line and
calls other functions.
1. A generator function that loops over filenames, opens each file,
loops over its lines, and yields one word at a time from the split
line.
1. A function that returns a counter from the generator returned by
the previous function.

To show that the counts are correct, you should call get the 10 most
common words using the `most_common` method on the counter and print
each word and its count. The output should look like the following:

<pre>
$ python count_words.py pp_ch1_tokenized.txt pp_ch2_tokenized.txt
54 you
48 the
47 of
42 i
41 to
32 and
31 a
27 that
27 it
26 not
</pre>

An example solution can be found in
[count_words.py](../examples/count_words.py).

## Normalized frequencies

It's useful to normalize counts by dividing by the total number of
words seen. Extend the previous exercise by writing a function
`normalize_counts` that takes a `Counter` as an argument and returns a
new `Counter` where each count is divided by the total of all
counts. Apply this function to the counts before printing them as
above. The output should look like:

<pre>
0.0328667072428 you
0.0292148508825 the
0.0286062081558 of
0.0255629945222 i
0.0249543517955 to
0.019476567255 and
0.0188679245283 a
0.0164333536214 that
0.0164333536214 it
0.0158247108947 not
</pre>
