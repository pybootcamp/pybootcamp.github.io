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
first paragraph of the first chapter of Pride and Prejudice:

<pre>
It is a truth universally acknowledged, that a single man in
possession of a good fortune, must be in want of a wife.
</pre>

We may want to transform this into a list of the individual words:

{% highlight python %}
['It', 'is', 'a', 'truth', 'universally', 'acknowledged,', 'that',
'a', 'single', 'man', 'in', 'possession', 'of', 'a', 'good',
'fortune,', 'must', 'be', 'in', 'want', 'of', 'a', 'wife.']
{% endhighlight %}

We can imagine a simple way to do this, assuming we have opened the
file already as `in_file`:

{% highlight python %}
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
words = [word for line in in_file for word in line]
{% endhighlight %}

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
