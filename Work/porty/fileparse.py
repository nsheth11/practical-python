# fileparse.py
#
# Exercise 3.3
import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', **opts):
    '''
    Parse a lines iterable into a list of records
    '''
    rows = csv.reader(lines, delimiter=delimiter)
    records = []

    #read options
    silence_errors = False
    if 'silence_errors' in opts:
        if opts['silence_errors'] == True:
            silence_errors = True

    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    # Read the file headers
    if has_headers:
        headers = next(rows)
        if select:
            indices = [ headers.index(s) for s in select ]
            headers = select
        else:
            indices = []
        
        for rownum,row in enumerate(rows, start=1):
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [ row[index] for index in indices]
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                record = dict(zip(headers, row))
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rownum, row)
                    log.debug("Row %d: Reason %s", rownum, e)
    else:
        for rownum, row in enumerate(rows, start=1):
            if not row:
                continue
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                records.append(tuple(row))
            except Exception as e:
                print(f'Bad row {rownum:d} : {row}')

    return records