---
layout: bare
title: Control flow
---
Use numbered headers: true

<h1>Contents</h1>
* TOC
{:toc}

# Iteration over sequences

# Enumerate

# `while` loops

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
