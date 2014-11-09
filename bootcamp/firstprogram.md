---
layout: bare
title: Writing your first program
---

# Contents
{:.no_toc}
1. TOC
{:toc}

# Basic math

To print something, just use `print`:
{% highlight python %}
>>> x = 7
>>> print x
7
{% endhighlight %}

`print` can work on any type. For our first program, we'll do some
simple arithmetic. Let's add two variables together and print the
output. Make a new file, enter this script, and run it:

{% highlight python %}
x = 7
y = 8
z = x + y
print z
{% endhighlight %}

How can you run a program? If you're using IDLE, hit F5. If you're
working from the command line, run the file, for example:  
`python test.py`

It should produce the output `15`. That was easy.

What if we divide instead? Change the crucial line to:
{% highlight python %}
z = x / y
{% endhighlight %}

We'll get `0`. Why is that? Well, by default, dividing an integer by
an integer in Python will always result in an integer. In this case,
it's rounded down, so we get zero. We can fix this by making one of
the numbers a `float`; division between a float and any other number
will produce a `float`.

We can make `y` a float by assigning it `8.0` instead of `8`, or by
just calling `float()` on it:

{% highlight python %}
z = x / float(y)
{% endhighlight %}

Now this prints `0.875`, as expected.

Check out the documentation on [Python Numeric
Types](http://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex)
for a full list of the arithmetic operators in Python.

At some point, if you've worked with another language you'll try to
write `x++` to add one to `x`. This doesn't work in Python. Instead,
write `x += 1`. Note that Python similarly supports `-=`, `*=`, and
`/=`.

# Simple loops

For the moment, we're going to explore the most basic loop in Python,
the `for` loop. We'll use it to iterate over a `list`, a data type
that we'll go over in more detail later. For now, think of a list as a
variable-sized array of ordered items. To initialize a list, we use
`[]` with commas to separate the items.

{% highlight python %}
letters = ['a', 'b', 'c']
{% endhighlight %}

This creates a list with three items in it. Python is zero-indexed, so
the first item is at position (index) zero, the second at position
one, etc.: `0: 'a'; 1: 'b'; 2: 'c'`.

So if we want to print each item in `letters`, we can write a loop as
follows:
{% highlight python %}
for item in letters:
    print item
{% endhighlight %}

Note that a `for` statement ends with a colon. The code that is inside
the loop _must be indented one level_. This will output:
{% highlight python %}
a
b
c
{% endhighlight %}

Note that each time you `print`, by default it puts each item on its
own line. If you don't want this, put a comma after the item being
printed:  
` print item,`

**Mini-assignment**: Clear out the above program. Without copying the
 above example, write a program where you put a few objects in a list
 and print them.

# Reading from files

One of the most common things we need to do is read data from
files. To open a file, simply use `open`. For now, let's work with the
[the first chapter of _Pride and Prejudice_](../examples/pp_ch1.txt).

To open it, after downloading it do the following:
{% highlight python %}
chapter = open("pp_ch1.txt", "U")
{% endhighlight %}

It's tempting to use simple names such as `file` or `input`; these are
both names of python built-in objects so best to leave them alone for
the moment. The first argument to `open` is the path to the file, the
second tells it what we want to do with it. In this case we're asked
for it to be opened in Universal newline mode, a way of reading files
that glosses over differences between Unix and Windows line endings.

# Functions

As we saw with `open`, we call a function in Python by using its name,
then following the name with parentheses which enclose the arguments.

Now we're going to write a simple function that prints all the lines
in a file. We're going to combine a `for` loop, using `open` to read a
file, and using `print` to output each line.

So, here's what this function will look like:

{% highlight python %}
def print_file(filename):
    """Print the contents of a file."""
    for line in open(filename, "U"):
    	print line.rstrip()
{% endhighlight %}

A few things to note:

1. We define a function by using the `def` keyword, then providing the
name of the function and the variable names we want to use for the
arguments given to it. Like `for`, `def` creates a block so we must
indent below.
1. Immediately after we declare the function, we write a triple-quoted
string under it describing what it does. (Don't worry about why it's
triple quotes right now.) This is called a _docstring_ and it is used
to explain what the function does.
1. When we print, we call the method `rstrip` on the string. This
removes any trailing whitespace. When reading a file, each line will
end with a newline marker until we explicitly remove it.

Functions can also return a value, for example we may want to set a
variable to the result of calling a function:
{% highlight python %}
def increment(num):
    """Return the input number increased by one."""
    return num + 1
{% endhighlight %}

**Mini-assignment**: Without copying the above example, write a
  function that takes two variables as arguments and returns the
  result of an arithmetic operation on them. For example, you could
  add two numbers together and return the result.

# Command-line arguments

We may want to be able to take arguments on the command line, for
example the name of the file whose contents we want to print. This is
accomplished through a list called `argv` available through the `sys`
module.

Accessing this can be demonstrated by the following program, which
I'll call `test.py`:
{% highlight python %}
import sys
print sys.argv
{% endhighlight %}
We need to test this from the command line, not inside another program
such as IDLE:
{% highlight bash %}
$ python test.py a b c
['test.py', 'a', 'b', 'c']
{% endhighlight %}

We notice that the first item appears to be the name of the script as
it was called; this is generally of little use. So we almost always
start looking at index 1, the second item. The line `import sys`
allows us to refer to the `sys` module. Even though it is built-in to
Python, we need to explicitly state that we are going to use it.

# Running a program

When you run a file like `test.py`, Python will compile the entire
file and execute anything that is at the outer level of
indentation. If your file defines functions but you want them to run
when the program is executed, you need to specify that. Here's a
modified version of the program above that demonstrates this:
{% highlight python %}
import sys


def print_args():
    """Print the command line arguments."""
    print sys.argv


if __name__ == "__main__":
    print_args()
{% endhighlight %}

This file defines the `print_args` function and then will run it the
file is run as a program. The purpose of the block under
`if __name__ == "__main__"` 
is so that if the file is imported--used to define functions--rather
than run as a main program, it won't run the `print_args` function,
just define it.

# Putting it all together

Now, to test your abilities, take on your first program. It is meant
to be a simplified version of `cat`, a tool which concatenates the
files given to it. It should:

1. Take a list of files to open as command line arguments.
1. For each file specified, print its contents.

For example, if we call `cat` on two files, the first of which
contains just the line `abc` and the second of which contains just the
line `def`, the output would be:  

<pre>
abc
def
</pre>

Try to do this without copy/pasting from the examples above. You'll
need to get all but the first element out of `sys.argv`. The easiest
way to do this is to do something like the following, which will be
explained soon:  
`filenames = sys.argv[1:]`

You can use the [first](../examples/pp_ch1.txt) and
[second](../examples/pp_ch2.txt) chapters of _Pride and Prejudice_ as
files to concatenate.

When you're done, take a look at [cat.py](../examples/cat.py) which
provides a solution.

If you want to write another simple program, write one that counts the
number of lines in a file. It should take the name of a single file as
a command line argument (which can be retrieved as `sys.argv[1]`),
count the number of lines in it, and print that number at the end. For
example:
{% highlight bash %}
$ python countlines.py pp_ch1.txt
111
{% endhighlight %}
