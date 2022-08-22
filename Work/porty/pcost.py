# pcost.py
#
# Exercise 1.27

from . import portfolio

import sys
import report

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

def portfolio_cost(filename):
    with open(filename, 'rt') as lines:
        port = portfolio.Portfolio.read_csv(lines)
        return port.total_cost

def main(argv):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"

    total_cost = portfolio_cost(filename)

    print(f'Total cost : {total_cost}')

if __name__ == '__main__':
    main(sys.argv)