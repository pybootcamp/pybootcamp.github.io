---
layout: bare
title: Basic data structures
---
Use numbered headers: true

<h1>Contents</h1>
* TOC
{:toc}

# Sequences

- Sequences types act as ordered containers, essentially arrays
- You can get to anything in them using an index, which starts at 0
- You can iterate over them
- The object in each bin is called an element

## List basics

For example, conisder the following `list` of strings:
{% highlight python %}
lyrics = ['Her', 'name', 'is', 'Rio']
{% endhighlight %}

Each string itself is actually its own container type, although it is
not a list. Lists are special in that you can modify their contents
and the items in them do not need to be the same type:
{% highlight python %}
lyrics[0] = 'His'
lyrics[3] = 7
{% endhighlight %}
You cannot change the contents of a string, but you can make a new
string instead.

## Working with lists

`len` returns the length of a sequence, which is the number of
items in it:
{% highlight python %}
>>> len(lyrics)
4
{% endhighlight %}

`[]` allow you to access elements in a list. If you ask
for an index that’s not in the sequence, you get an error. In addition
to the usual indices, you can ask for negative indices, which go from
the end of the sequence
{% highlight python %}
>>> lyrics[0] # The first element
'Her'
>>> lyrics[4]
IndexError: list index out of range
>>> lyrics[-1] # The last element
'Rio'
>>> lyrics[-2] # The second-to-last element
'is'
{% endhighlight %}

You can get more than one element at a time via _slicing_. Slicing
gets you an ordered subsequence of the list between two indices,
_inclusive_ of the first index, and _exclusive_ of the second. To
slice use the colon:
{% highlight python %}
>>> lyrics = ['Her', 'name', 'is', 'Rio']
>>> lyrics[0:1] # From 0 to before 1
['Her']
>>> lyrics[0:2] # From 0 to before 2
['Her', 'name']
>>> lyrics[1:]  # From 1 to the end
['name', 'is', 'Rio']
>>> lyrics[:-1] # From start to before -1
['Her', 'name', 'is']
>>> lyrics[:] 	 # From start to the end 
['Her', 'name', 'is', 'Rio']
>>> lyrics[-2:] # From -2 to end
['is', 'Rio']
{% endhighlight %}

The `for` loop gives simple iteration over sequences. Read this as
"Each time the loop runs, set `item` equal to the next element in
`items`.  We call `item` a _loop variable_, meaning it's the main
variable that changes as the loop runs.

{% highlight python %}
for item in items:
    print item
{% endhighlight %}

If we need to do something with the index as well, `enumerate` can be
used. "Each time the loop runs, set `item` equal to the next element
in items and set `index` to the index of that item.

{% highlight python %}
for index, item in enumerate(items):
    print item, "is at index", index
{% endhighlight %}

Note two useful syntactic tidbits there. First, you can automatically
_unpack_ the index and item at once. You can also print multiple
things by separating them with a comma, which will put a space between
them.

You can add one item to a list by using `append`, or multiple by using
`extend`:

{% highlight python %}
>>> lyrics = ['Her', 'name', 'is', 'Rio']
>>> lyrics.append('and')
>>> lyrics
['Her', 'name', 'is', 'Rio', 'and']
>>> lyrics.extend(['she', 'dances', 'on', 'the', 'sand'])
>>> lyrics
['Her', 'name', 'is', 'Rio', 'and', 'she', 'dances', 'on', 'the', 'sand']
{% endhighlight %}

Note that these change this list in place but don't return
anything. Don't make the mistake of writing something like:

{% highlight python %}
# This is pointless, lyrics2 will be None
lyrics2 = lyrics.append('and')
{% endhighlight %}


# Maps

- Maps store a relationship between two things, a _key_ and a
_value_.
- The only map we care about is a dictionary, the type `dict`.
- You look up information by giving a key and you get back a
value. It's like a book’s index: the keys are words, the values are
page numbers.
- The time to look up something in a dictionary is roughly constant
and not affected by how many things are in the dictionary. This is
unlike a `list`, where to find an item you have to check each element.

Curly braces (`{}`) are in the creation of dictionaries, while square
braces (`[]`) are used for lookup, just like lists.

{% highlight python %}
Creating a new empty dictionary
nums_to_words = {}
# Assigning a value to a key in the dictionary
nums_to_words[1] = 'one'
# Getting a value from the dictionary using a key
word = nums_to_words[1]
# Deleting a key from the dictionary
del nums_to_words[1]
# Creating a new dictionary with items in it
nums_to_words = {1: 'one', 2: 'two', 3: 'three'}
{% endhighlight %}

In this example the keys of the dictionary are integers, which
highlights the facts that just by looking at it it's hard to tell
what's different between a `list` and `dict`. The keys in a `dict` can
be any _immutable_ type, which we'll define later, but for the moment
contains strings, integers, and tuples but not lists or dictionaries.

You can iterate over keys, values, or both using a for loop
{% highlight python %}
# Loop over keys
for key in adict:
    print "Key:", key

# Loop over values
for value in adict.values():
    print "Value:", value

# Loop over both
for key, value in adict.items():
    print "Key", key, "has value", value
{% endhighlight %}

Checking whether a key is in the dictionary is easy
{% highlight python %}
if key in adict:
    print "Found key", key
{% endhighlight %}

What if a key doesn't exist? An _exception_ occurs.
{% highlight python %}
>>> nums_to_words = {1:'one', 2:'two', 3:'three'}
>>> nums_to_words[1]
'one'
>>> nums_to_words[4]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nums_to_words[4]
KeyError: 4
{% endhighlight %}

You can fix this by either checking in advance for whether a key is in
the dictionary or by handling the exception, which we'll talk about
later.

# String formatting

You often want to print out strings nicely, as a part of normal
operation or debugging. This is best accomplished by using the
`format` method on a string.

{% highlight python %}
>>> lyrics = ['Her', 'name', 'is', 'Rio']
>>> print "lyrics contains {} items".format(len(lyrics))
lyrics contains 4 items
{% endhighlight %}

The `format` method replaces areas marked with `{}` with its
arguments. You can use this to this to control the details of what
goes in. For example:
{% highlight python %}
>>> print "Lyrics: {}".format(lyrics)
Lyrics: ['Her', 'name', 'is', 'Rio']
>>> print "First word: {}".format(lyrics[0])
First word: Her
>>> print "First word: {!r}".format(lyrics[0])
First word: 'Her'
>>> print "2/3 is {}".format(2.0 / 3.0)
2/3 is 0.666666666667
>>> print "2/3 is {:0.2f}".format(2.0 / 3.0)
2/3 is 0.67
{% endhighlight %}

By default, format coaxes its arguments into the prettiest strings
possible. Using `{!r}` calls `repr` on the argument, which makes the
representation "machine-readable" by adding things like quotation
marks around it and sometimes type information. Other format
specifiers can do things like control the number of digits
displayed. See the [format string
specification](http://docs.python.org/2/library/string.html#formatstrings)
for the gory details.

# Data model

As alluded to earlier, some types of data can be changed in-place
while others cannot. The `tuple` is a type similar to a list but one
that cannot be changed once it is created; it is _immutable_.

{% highlight python %}
>>> words1 = ['the', 'dog']
>>> words1[1] = 'cat'
>>> words1
['the', 'cat']
>>> words2 = ('the', 'dog')
>>> words2[1] = 'cat'
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    words2[1] = 'cat'
TypeError: 'tuple' object does not support item assignment
{% endhighlight %}

This manifests itself when considering the question "will changing
this object affect anything else?". For example:
{% highlight python %}
>>> x = 7
>>> y = 7
>>> x += 1
>>> x
8
>>> y
7
{% endhighlight %}

As integers are immutable, at the beginning `x` and `y` refer to the
same object but when `x` is incremented it points to a different
object instead. However, note:

{% highlight python %}
>>> x = ['a']
>>> y = x
>>> x.append('b')
>>> x
['a', 'b']
>>> y
['a', 'b']
{% endhighlight %}

As lists are mutable, `append` changes the object in-place, affecting
`x` and `y`.
