import fileinput
import sys


def main():
    if len(sys.argv) < 2:
        print('''Usage: awpie 'prog' [file ...]''', file=sys.stderr)
        return 1

    sep = None
    prog = sys.argv[1]
    files = ['-']
    if len(sys.argv) >= 3:
        files = sys.argv[2:]

    for line in fileinput.input(files=files):
        line = line.strip('\r\n')
        fields = line.split(sep)
        exec(prog, None, {
            'line': line,
            'fields': fields,
            'stdout': sys.stdout,
            'stderr': sys.stderr,
            'filename': fileinput.filename(),
            'fileno': fileinput.fileno(),
            'lineno': fileinput.lineno(),
            'filelineno': fileinput.filelineno(),
            'isfirstline': fileinput.isfirstline(),
            'isstdin': fileinput.isstdin(),
            'nextfile': fileinput.nextfile,
        })


if __name__ == '__main__':
    main()
