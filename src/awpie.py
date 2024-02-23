import collections
import fileinput
import functools
import getopt
import importlib
import itertools
import operator
import os
import sys


# Make some linters (pyright) happy.
_ = collections
_ = functools
_ = itertools
_ = operator
_ = os


class UserData(dict):
    def __getattr__(self, key):
        if key not in self:
            raise AttributeError(key)
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


def main():
    usage = '''Usage: awpie [--sep=separator] [--imports=module1,module2] [--begin='prog'] [--end='prog'] 'prog' [file ...]'''

    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['sep=', 'imports=', 'begin=', 'end='])
    except getopt.GetoptError as err:
        print(err, file=sys.stderr)
        print(usage, file=sys.stderr)
        return 1
    if not args:
        print(usage, file=sys.stderr)
        return 1

    prog = args[0]
    data = UserData()
    files = ['-']
    if len(sys.argv) >= 2:
        files = args[1:]
    sep = None
    begin = ''
    end = ''
    for o, a in opts:
        if o == '--sep':
            sep = a
        elif o == '--imports':
            modules = a.split(',')
            for m in modules:
                if not m:
                    continue
                m = m.strip()
                globals()[m] = importlib.import_module(m)
        elif o == '--begin':
            begin = a
        elif o == '--end':
            end = a

    exec(begin, None, {'data': data})

    for line in fileinput.input(files=files):
        line = line.strip('\r\n')
        fields = line.split(sep)
        exec(prog, None, {
            'line': line,
            'fields': fields,
            'data': data,
            'stdout': sys.stdout,
            'stderr': sys.stderr,
            'filename': fileinput.filename(),
            'fileno': fileinput.fileno(),
            'lineno': fileinput.lineno(),
            'filelineno': fileinput.filelineno(),
            'isfirstline': fileinput.isfirstline(),
            'isstdin': fileinput.isstdin(),
            'nextfile': fileinput.nextfile,
            'close': fileinput.close,
        })

    exec(end, None, {'data': data})


if __name__ == '__main__':
    main()
