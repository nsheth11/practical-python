#!/Users/nsheth/anaconda3/bin/python3
# report.py
#
# Exercise 2.4
import csv
import sys
from this import d
from . import portfolio
from . import fileparse
from . import stock
from . import tableformat


def read_portfolio(filename, **opts):
    '''
    This function reads a file and prepares portfolio list
    '''
    with open(filename, 'rt') as lines:
        port = portfolio.Portfolio.read_csv(lines, **opts)
        return port

def read_prices(filename):
    '''
    This function reads stocks and their current prices from a csv file and returns dictionary with name and price
    '''
    with open(filename, 'rt') as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report(port, prices):
    '''
    This function prepares report of current portfolio for each holding given current prices
    '''
    report = []

    for holding in port:
        curprice = prices[holding.name]
        shares = holding.shares
        report.append((holding.name, shares, curprice, curprice - holding.price))

    return report

def print_report(report, formatter):
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
    formatter.finish()


def portfolio_report(portfile, pricefile, fmt='txt'):
    port = read_portfolio(portfile)
    prices = read_prices(pricefile)
    #formatter = tableformat.TextTableFormatter()
    formatter = tableformat.create_formatter(fmt)
    
    print_report(make_report(port, prices), formatter)

def main(argv):
    if ( len(argv) < 3):
        raise Exception('Incorrect number of arguments')
    
    portfile = argv[1]
    pricefile = argv[2]
    fmt = 'txt'
    if len(argv) == 4:
        fmt = argv[3]
    portfolio_report(portfile, pricefile, fmt)

if __name__ == '__main__':
    main(sys.argv)


