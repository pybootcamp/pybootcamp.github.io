---
layout: bare
title: Control flow
---
Use numbered headers: true

<h1>Contents</h1>
* TOC
{:toc}

# Iteration over sequences

In previous sections, we've covered how to iterate over sequences
using `for`. We'll go over ways _not_ to iterate over sequences in the
next section.

Some things we didn't mention earlier:
- You can use the `break` command to exit from a `for` loop
prematurely. For example, if you were looking for one thing and you
found it, you might `break` rather than wasting time processing the
rest of the entries.
- You can use `continue` to skip to the next entry. For example, if
you only want to process words that start with `'a'`, you might check
whether each item starts with that and skip the others.

{% highlight python %}
for item in items:
    if item[0] != 'a':
        continue
    else:
        do_something(item)
{% endhighlight %}


# Basic conditionals

The previous example brought up the basic structure of a Python
conditional. It looks like this:

{% highlight python %}
def test(x):
    """Print whether the argument evaluates as True or False."""
    if x:
        print 'Evaluated as True'
    else:
        print 'Evaluated as False'
{% endhighlight %}

Python has two built-in boolean constants `True` and `False`, but you
usually don't need to compare directly against them. You can specify
"else if" clauses using `elif`.

# `while` loops

Sometimes you are not sure when you'll be done processing data. For
example, let's say you want to process data until some falg is set,
but you don't have a list of it at the beginning. The solution is to
use a `while` loop. Assume for the moment you have a variable `done`
that you will use to record whether you're done:

{% highlight python %}
while not done:
    # Call a magic function to do work
    result = perform_work()
    # Set done if appropriate
    done = is_good_enough(result)
{% endhighlight %}

This loop will automatically stop running when `done` is set to `True`.

# Exceptions

- An exception is raised when something goes wrong.
- If an exception is unhandled, it will crash your program.
- If an exception is handled, your program can take some corrective action and continue.
- So any exceptions that you expect to occur during the normal operation of your program should be handled.

Handling is accomplished with a try…except block:
{% highlight python %}
try:
    # Do something risky here
except <name of exception to catch>:
    # Take some non-risky corrective action
{% endhighlight %}
