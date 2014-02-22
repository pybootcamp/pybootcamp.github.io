---
layout: bare
title: Anti-Patterns in Python Programming
---
Use numbered headers: true

<h1>Contents</h1>
* TOC
{:toc}

# Iteration
## The use of `range`
Programmers that are new to Python love using `range` to
  perform simple iteration by applying it over the length of an
  iterable and then getting each element:

{% highlight python %}
for i in range(len(alist)):
    print alist[i]
{% endhighlight %}

Recite it in your sleep: `range` is not for simple, obvious iterations over sequences. 
For those used to numerically defined `for` loops, `range` feels like home, 
but using it for iteration over sequences is bug-prone and less clear than using the standard 
`for` construct directly on an iterable. Just write:

{% highlight python %}
for item in alist:
    print item
{% endhighlight %}

Misuses of `range` are prone to unfortunate off-by-one bugs. This is
commonly caused by forgetting that `range` is inclusive in its first
argument and exclusive in its second, just like [`substring` in
Java](http://download.oracle.com/javase/6/docs/api/java/lang/String.html#substring\(int\))
and many, many, other functions of this type.  Those who think too
hard about not overrunning the end of their sequence are going to
create bugs:

{% highlight python %}
# An incorrect way to iterate over a whole sequence
alist = ['her', 'name', 'is', 'rio']
for i in range(0, len(alist) - 1): # Off by one!
    print i, alist[i]
{% endhighlight %}

The common excuses for using `range` inappropriately are:

<ol>
  <li><p>Needing the index value in the loop. This isn't a valid
excuse. Instead, you should write:</p>
    {% highlight python %}
    for index, value in enumerate(alist): 
        print index, value
    {% endhighlight %}</li>

  <li><p>Needing to iterate over two loops at once, getting a value at
the same index from each. In this case, you want to
use <a href="http://docs.python.org/2/library/functions.html#zip"><code>zip</code></a>:</p>
    {% highlight python %}
    for word, number in zip(words, numbers):
        print word, number
    {% endhighlight %}</li>

  <li><p>Needing to iterate over only part of a sequence. In this case, just
iterate over a slice of the sequence and include a comment to make it
clear that this was intentional:</p>
    {% highlight python %}
    for word in words[1:]: # Exclude the first word
        print word
    {% endhighlight %}
  <p>An exception to this is when you're iterating over a sequence so
big that the overhead introduced by slicing the would be very
expensive. If your sequence is 10 items, this is unlikely to matter,
but if it is 10 million items or this is done in a
performance-sensitive inner loop, this is going to be very
important. Consider using
<a href="http://docs.python.org/2/library/functions.html#xrange"><code>xrange</code></a>
in this case.</p>
  </li>
</ol>

An important use case of `range` outside of iterating over a sequence
is when you genuinely need a list of numbers not to be used for indexing:
{% highlight python %}
# Print foo(x) for 0<=x<5
for x in range(5):
    print foo(x)
{% endhighlight %}

## Using list comprehensions properly
If you have a loop that looks like this, you want to rewrite it as a list
comprehension:
{% highlight python %}
# An ugly, slow way to build a list
words = ['her', 'name', 'is', 'rio']
alist = []
for word in words:
    alist.append(foo(word))
{% endhighlight %}

Instead, write a list comprehension:
{% highlight python %}
words = ['her', 'name', 'is', 'rio']
alist = [foo(word) for word in words]
{% endhighlight %}

Why do this? For one, you avoid any bugs related to correctly initializing 
alist. Also, the code just looks a lot cleaner and what you're doing is clearer.
For those from a functional programming background, 
<a href="http://docs.python.org/library/functions.html#map"><code>map</code></a>
may feel more familiar, but I find it less Pythonic.
 
Some common excuses for not using a list comprehension:

<ol>
  <li><p>You need to nest your loop. You can nest entire list
      comprehensions, or just put multiple loops inside a list
      comprehension. So, instead of writing:</p>

    {% highlight python %}
    words = ['her', 'name', 'is', 'rio']
    letters = []
    for word in words:
        for letter in word:
            letters.append(letter)
    {% endhighlight %}

    <p>Write:</p>

    {% highlight python %}
    words = ['her', 'name', 'is', 'rio']
    letters = [letter for word in words
                      for letter in word]
    {% endhighlight %}
    
    <p>Note that in a list comprehension with multiple loops, the loops have the same order as 
    if you weren't making a list comprehension at all.</p></li>

  <li><p>You need a condition inside your loop. But you can do this in a list
  comprehension just as easily:</p>

    {% highlight python %}
    words = ['her', 'name', 'is', 'rio', '1', '2', '3']
    alpha_words = [word for word in words if isalpha(word)] 
    {% endhighlight %}</li>
</ol>

A valid reason for not using a list comprehension is that you can't do
exception handling inside one. So if some items in the iteration will
cause exceptions to be raised, you will need to either offload the
exception handling to a function called by the list comprehension or
not use a list comprehension at all.

---

# Performance Pitfalls
## Checking for contents in linear time
Syntactically, checking if something is contained in a list or a set/dictionary look alike, 
but under the hood things are different. If you need to repeatedly check whether something is contained 
in a data structure, use a set instead of a list. (You can use a dict if you need to associate a 
value with it and also get constant time membership tests.)
 
{% highlight python %}
# Avoid this
lyrics_list = ['her', 'name', 'is', 'rio']
words = make_wordlist() # Pretend this returns many words that we want to test
for word in words:
    if word in lyrics_list: # Linear time
        print word, "is in the lyrics"
{% endhighlight %}

{% highlight python %}
# Do this
lyrics_list = ['her', 'name', 'is', 'rio']
lyrics_set = set(lyrics_list) # Linear time set construction
words = make_wordlist() # Pretend this returns many words that we want to test
for word in words:
    if word in lyrics_list: # Constant time
        print word, "is in the lyrics"
{% endhighlight %}

Keep in mind that creation of the set will take linear
time even though membership testing takes constant time. So if you are
checking for membership in a loop, it's almost always worth it to take
the time to build a set since you only have to build the set once.

---

# Leaky Variables

## Loops
Generally speaking, in Python the scope of a name is wider than one
  might expect given other languages. For example, in Java, the
  following code will not even compile:

{% highlight java %}
// Get the index of the lowest-indexed item in the array
// that is > maxValue
for(int i = 0; i < y.length; i++) {
    if (y[i] > maxValue) {
        break;
    }
}
// Oops, there is no i here
processArray(y, i);
{% endhighlight %}

However, in Python the equivalent will always compile and often
produce the intended result:

{% highlight python %}
for idx, value in enumerate(y):
    if value > max_value:
        break
    
processList(y, idx)
{% endhighlight %}

This will work in all cases except when `y` is empty; in that case the
loop never runs and the call to `processList` will raise a `NameError`
because `idx` is not defined. If you use Pylint, it would warn you
about "Using possibly undefined loop variable idx."

The solution is to always be explicit and set `idx` to some special
value before the loop, so you know what to look for if the loop never
runs. This is called the [Sentinel
Pattern](http://c2.com/cgi/wiki?SentinelPattern). So what value should
you use for a sentinel? Starting with C or earlier, back when `int`
ruled the Earth, a common pattern for a function that needed to return
an "expected error" result was to return `-1`. For example,
let's say you want to return the index of an item in a list:

{% highlight python %}
def find_item(item, alist):
    # None is arguably more Python than -1
    result = -1
    for idx, other_item in enumerate(alist):
        if other_item == item:
            result = idx
            break

    return result
{% endhighlight %}

In the general case, `None` is a better sentinel of choice in Python,
even if it isn't used consistently by Python's standard types (e.g.,
`str.find`). See the style section for recommended ways to test for
None.

## The outer scope

Programmers new to Python often love to put everything in what is
called the _outer scope_, the parts of a python file not
contained in a block such as a function of class. The outer scope
corresponds to the _global_ namespace; for the purpose of this
discussion, you should assume the contents of the global namespace are
accessible anywhere within a single Python file.

The outer scope is great for defining constants that the whole module
needs access to that you want to declare at the top of a file. It's
wise to give anything in the outer scope distinctive names, for
example `IN_ALL_CAPS`. That makes it easier to avoid bugs like the
following:

{% highlight python %}
import sys

# See the bug in the function declaration?
def print_file(filenam):
    """Print every line of a file."""
    with open(filename) as input_file:
        for line in input_file:
            print line.strip()
            
if __name__ == "__main__":
    filename = sys.argv[1]
    print_file(filename)
{% endhighlight %}

If you look closely, you'll see that the definition of `print_file`
names its argument `filenam`, but the body of the function references
`filename`. However, this program works just fine. Why? In
`print_file` when a local variable named `filename` isn't found, the
next step is to look at the global namespace. Since the code that
calls print_file lives in the outer scope (even though it's indented),
the variable filename declared there is visible to `print_file`.

So, how do you avoid problems like this? First, don't set any values
in the outer scope that aren't `IN_ALL_CAPS`. Things like parsing
arguments are best delegated to a function named `main`, so that any
internal variables in that function do not live in the outer scope.

This also serves as a reminder about the `global` keyword. _You do not
need the global keyword if you are just reading the value of a global
name._ You only need it if you want to change what object a global
variable name refers to. See [this discussion of the global keyword on
Stack Overflow](http://stackoverflow.com/a/4693170/944164) for more
information.

---

# Style, style, style

## Honor thy PEP 8

[PEP 8](http://www.python.org/dev/peps/pep-0008/) is the universal
style guide for Python code. You should know it by heart and follow it
as much as possible, although some folks for good reason may disagree
on small issues like the amount of indentation or blank lines to
use. If you aren't following it, you should have good reasons beyond
"I just don't like the way that looks." The guidelines below
are all taken from PEP 8 and seem to be the ones people need to be
reminded of most often.

## Testing for empty

If you want to check whether a container type (e.g., list, dictionary,
set) is empty, simply test it instead of doing something
  like `len(x) > 0`:

{% highlight python %}
numbers = [-1, -2, -3]
# This will be empty
positive_numbers = [num for num in numbers if num > 0]
if positive_numbers:
    # Do something awesome
{% endhighlight %}

If you want to store this result somewhere, use
`bool(positive_numbers)`; `bool` is what is called to determine the
truth value of the target of `if`.

## Testing for `None`

As I mentioned previously, `None` makes a good sentinel
  value. How should you check for it?

If you are specifically testing for `None` and not just
  other things that evaluate as `False` (e.g., empty
  containers, 0) use `is`:

{% highlight python %}
if x is not None:
    # Do something with x
{% endhighlight %}

If you are using `None` as a sentinel, this is the
  desired pattern; you want to distinguish `None` from 0,
  for example.

If you are just testing for whether you have something useful to
  work with, a simple if pattern is usually good enough:

{% highlight python %}
if x:
    # Do something with x
{% endhighlight %}

For example, if `x` is expected to be a container type, but could be
`None` based on the result of another function, this handles all the
cases that you care about at once. Just be aware that if you change
the value that goes into `x` such that `True` or `0.0` are useful
values, this may not behave the way you want.
