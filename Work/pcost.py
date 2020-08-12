# pcost.py
#
# Exercise 1.27

#The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding.
#Write a program called pcost.py that opens this file, reads all lines, and
#calculates how much it cost to purchase all of the shares in the portfolio.
#Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).


import csv

def portfolio_cost(filename):
    total_cost = 0
   
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError:
                print('Bad row:', row)
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
