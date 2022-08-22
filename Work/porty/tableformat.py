# tableformat.py

class FormatError(Exception):
    pass


class TableFormatter:

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError
    
    def finish(self):
        raise NotImplementedError

class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
    def finish(self):
        pass

    

class CSVTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers), end=' ')
        print()

    def row(self, rowdata):
        print(','.join(rowdata), end=' ')
        print()
    def finish(self):
        pass

class HTMLTableFormatter(TableFormatter):

    '''
    Output data in HTML table format.
    '''
    def headings(self, headers):
        print('<html><body><table>', end='')
        print()
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
        
    def finish(self):
        print('</table></body></html>')

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')

    return formatter

def print_table(portfolio, cols, formatter):
    formatter.headings(cols)

    for holding in portfolio:
        rowdata = []
        for col in cols:
            field = getattr(holding,col)

            if type(field) == int:
                rowdata.append(str(field))
            elif type(field) == float:
                rowdata.append(f'{field:0.2f}')
            else:
                rowdata.append(field)
        formatter.row(rowdata)

    formatter.finish()