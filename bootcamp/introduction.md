---
layout: bare
title: Introduction
---

# Contents
{:.no_toc}
1. TOC
{:toc}

# Why use Python?

1. Python is powerful and easy.  
![xkcd comic on Python](http://imgs.xkcd.com/comics/python.png)
1. Python comes with "batteries included." There are lots of useful
and powerful packages in the standard library.
1. Whitespace is required, preventing hopelessly unreadable code
1. Programs are short, clear, and concise
1. You don’t have to use object-oriented programming when it isn’t appropriate
1. There’s one obvious way to do it
1. Easy inheritance from built-in types
1. A simple data model

# Some challenges in dealing with Python

1. “Variables” as you know it don’t exist. The _names_ that
replace them take some getting used to.
1. The compiler will not stop you from shooting yourself in the foot
1. No enforcement of contracts/interfaces
1. Lots of things can go wrong at runtime that are hard to see coming

# How Python works

1. Each line of code is parsed into its syntax
1. The syntax tree is turned into _byte code_ which is executed by the
_interpreter_
1. Only syntax errors are caught in advance; _runtime_ errors are
reported as they happen

# Some basics

1. Start out by running `python` or `IDLE` to try out typing things in
the interpreter.
1. Typing directly into the interpreter is called a `REPL`: Read Eval
Print Loop. It reads your input line-by-line and prints results.

## Literals
The simplest thing you can type is an _expression_. The simplest
expressions are just literals, which evaluate to themselves. Note that
Python uses single and double-quotes interchangeably, and doesn't
distinguish between _characters_ and _strings_ like many other languages.
{% highlight python %}
>>> 7
7
>>> 7.5
7.5
>>> "H"
'H'
>>> "Hello world!"
'Hello world!'
{% endhighlight %}

## Assignment
You don't have to do much work to assign values to variables. What
are called "variables" in most programming languages are technically called
"names" in Python. We'll worry about what that means later.
{% highlight python %}
>>> x = 7
>>> x
7
>>> x = 7.5
>>> x
7.5
>>> x = "H"
>>> x
'H'
>>> x = "Hello world!"
>>> x
'Hello world!'
{% endhighlight %}

Note that you don't have to declare variables in advance and you don't tell
Python what _type_ (string, integer, etc.) a variable will have.

## Handy built-in functions

These are very useful when you're trying to sort out issues in the REPL.
You'll rarely need to use these in real programs.

- `type(x)`: see what type `x` is
{% highlight python %}
>>> type(7)
<type 'int'>
>>> type(7.0)
<type 'float'>
>>> type("H")
<type 'str'>
>>> type("Hello world!")
<type 'str'>
{% endhighlight %}
- `dir()`: see what names are bound at the moment
- `dir(x)`: see all methods that `x` provides
- `id(x)`: get the identity (effectively memory address) of what `x` refers to.
