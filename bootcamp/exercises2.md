---
layout: bare
title: Intermediate exercises
---
Use numbered headers: true

<h1>Contents</h1>
* TOC
{:toc}

# Presidential ratings

Skills used: CSV reading, basic math, dealing with data

Your task is to write a program that summarizes the data contained in
[presidents.csv](../examples/presidents.csv). This contains data from
the `presidents` dataset in R, quarterly approval ratings of US
presidents. Your program `avg_ratings.py` should take two filenames as
command-line arguments: the CSV file to read (`presidents.csv`) and
the output filename.

The input file contains three columns: `id` is a unique identifier for
each row, `year` gives the year and quarter of the rating, and
`rating` gives the approval rating.

You should write your output to a new CSV with three columns: `year`
will contain whole years (i.e., `1975` but no information about
specific quarters), `mean` will have the mean approval rating for that
year, and `median` will have the median approval rating for that year.

As some quarters are missing ratings (`NA`) you will have to exclude
those from the mean/median calculations. You should write functions to
calculate the mean and median of a list of numbers and remove any `NA`
from the list before passing it to those functions.

Your output should look like the following for the first five years:

<pre>
year,mean,median
1945,81.33333333333333,82
1946,47.0,46.5
1947,51.0,57.0
1948,37.5,37.5
1949,58.5,57.0
1950,41.75,41.5
</pre>

An example solution is available in
[avg_ratings.py](../examples/avg_ratings.py).

# Employee database

Skills used: Listing directory contents, classes, string parsing

Your task is to write a program that aggregates data spread across a
number of files. Start by downloading the file
[employee_info.zip](../examples/employee_info.zip) and unzipping it to
create a folder named `employee_info`.

In this folder, there's a set of files of the format `<employee id>.txt`
with information about each employee. For example, `372.txt` contains
the following:

<pre>
Name: John Smith
Title: Researcher
</pre>

You should write a program that reads in every file in the
`employee_info` folder and stores the data in a dictionary. Each key
for the dictionary should be the employee ID (which is numeric, but
you can treat it as a string without any problems), and each value
should be a object of the class `Employee`.

You should define the class `Employee` yourself such that:

1. It has an `__init__` function that takes the employee name, id, and
title as arguments and stores them in the class.
1. It has a `__str__` function that allows for nice, human-readable
printing of the object. For example, in might return: `John Smith,
Researcher (372)`.

Your program should:

1. Take the target directory (`employee_info`) as a command-line
argument.
1. List the contents of the directory.
1. Open each file in the directory and store the information in that
file in a new `Employee` object in the dictionary.
1. At the end, print out all of the key-value pairs of the dictionary,
one per line, separated by a colon. For example, a line would be: 
`372: John Smith, Researcher (372)`.

Hints:

1. You will need to put together the name of the directory of files
and the individual filenames in order to open them. Use
`os.path.join`.
1. You can assume the first line of each file contains the name field
and that the second line contains the title field. (If you want an
extra challenge, write a solution that does not make this assumption.)
1. You can use `split` to parse each string in the file. If you want
an additional challenge, use a regular expression, using the module `re`.
1. You should not assume that a name only consists of a first and last
name; your solution should still work if the name is "John Q Public."
If you notice that you are only extracting the first name, you are
probably using `split` incorrectly.

An example solution is available in
[employee_info.py](../examples/employee_info.py).


# On your own

Now's a great time to come up with your own exercise and try it out!
