---
layout: bare
title: Using the CSV module
---

<h1>Contents</h1>
* TOC
{:toc}

# Understanding CSVs

A comma-separated values (CSV) file is a convenient way to store data
that can be easily read and written. Despite the name, many CSVs files
aren't even comma-delimited (tab is common, but people rarely call
them TSV) and there is no standard way of doing it.

You might think you can trivially read and write CSVs using
`.split(',')` to read them and `','.join(fields)` to write
them. However, this is risky; if some of the fields contain commas
themselves, those fields will be enclosed by quotes and you'll end up
misparsing.

## Reading a CSV

The simplest way to read a CSV is the
[`csv.reader`](http://docs.python.org/2/library/csv.html#csv.reader)
function. This will return a reader object that allows you to read
each row as a list. An example adapted from the documentation:
{% highlight python %}
>>> import csv
>>> with open('eggs.csv', 'U') as csvfile:
...     spamreader = csv.reader(csvfile)
...     for row in spamreader:
...         print ', '.join(row)
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
{% endhighlight %}

This demonstrates another useful Python construct, using `with` to
mark of a block where you will use a file, which will automatically
close it when you are done with it.

## Writing a CSV 

Similarly,
[csv.writer](http://docs.python.org/2/library/csv.html#csv.writer)
allows you to write a CSV by writing one row at a time.  Note that
when you write a CSV file, you want to set the mode to `'wb'`.

## DictReader/Writer

What if you don't want to rely on hard-coding the order of the fields
in each line? You can use the
[`DictReader`](http://docs.python.org/2/library/csv.html#csv.DictReader)
and
[`DictWriter`](http://docs.python.org/2/library/csv.html#csv.DictWriter)
classes to help. These allow you to read and write each row as a
dictionary, with keys being the field names and values being the value
of that field in each row.

# Too slow?

The standard Python CSV parser is designed to handle a lot of strange
input well, including Excel files. If you care more about speed than
broad features, take a look at [`read_csv` in
pandas](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.parsers.read_csv.html). 

# Exercises

Here are some exercises to get you used to working with the CSV
module. Try these out using a [sample CSV
file](../examples/csv_data.csv).

1. Write a function that reads a CSV and uses a `defaultdict` to store
a list of the values for each item as it reads in the CSV. Use
`csv.reader` and `csv.writer`.
1. Write a second function that takes the dictionary produced above
and then computes the minimum, maximum, and mean values for each
item. (You'll need to write your own function to compute the mean.)
Write these values to another CSV with four fields: `item, min, mean,
max`.
1. When you've got everything working, replace the reader and writer
with `csv.DictReader` and `csv.DictWriter`.
