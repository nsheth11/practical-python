# ticker.py

from mailbox import FormatError
from . import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows
def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
def ticker(portfile, logfile, fmt):
    from . import report
    from . import tableformat

    portfolio = report.read_portfolio(portfile)
    lines = follow.follow(logfile)
    rows = parse_stock_data(lines)
    #rows = filter_symbols(rows, portfolio)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )
    formatter.finish()


if __name__ == '__main__':
    from . import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    lines = follow.follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows,portfolio)
    for row in rows:
        print(row)