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
presidents.

The csv file contains three columns: `id` is a unique identifier for
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
