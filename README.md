# python-challenge
This is a set of programs that analyzes bank and election data while learning basic python.

PyBank
======


For this challenge we are given a dataset describing monthly profit/loss data for a company, and we had to summarize the data in various ways.

The program I wrote reads the data and calculates the total number of months in the data, the net profit (or loss) for the company over that time period, and the average profit/loss over the time period.

To calculate average change, I took advantage of a formula that only requires using the first value in the series and the last value, since the values in between are said to form a telescoping series.

In other words, if you have a series of data (a, b, c, d, e), and you want to find the average change, you would first calculate the change from each value to the next:

b – a, c – b, d – c, e – d

Then you would add these values and divide by the number of changes measured. Notice what happens to the sum of these values when we rearrange them:

(b – a) + (c – b) + (d – c) + (e – d) =

b - a + c - b + d - c + e - d =

-a + b - b + c - c + d - d + e =

e - a

We are left with the very last value, e, minus the very first value, a.


This program also finds the month with the greatest increase and the greatest decrease (reporting both the month and the amount).


Another thing to note about my program is that I wanted to find a way to format negative numbers and include the "$' symbol in the report, and I was able to do this by creating a function that returns a formatted string in either case (whether it is a profit or loss).


Finally, the information is printed to the terminal and written to a text file.


PyPoll
======


For this challenge, we were given a set of data that included vote totals from a region holding an election. We did not necessarily know how many candidates were running, or any other information (such as party affiliation, poll predictions, voter demographics, etc.) Our challenge was simply to tally the votes each candidate received and declare a winner by popularity.

I decided to build a dictionary of vote totals since each candidate needed to be tracked individually as the votes were tallied, and a dictionary allowed me to reference a candidate by name instead of assigning them an arbitrary number. This was also useful since we didn't know the candidates beforehand, so my program adds any new names it encounters in the vote tally as a new candidate, building the list of candidates along the way.

In order to provide vote totals and percentages for each candidates, I used a for loop that created a string and added that to a list that could be used to print to the terminal or write lines to a text file.

Finally, when all the information was printed to the terminal and a winner determined, my program writes these results to a text file.
