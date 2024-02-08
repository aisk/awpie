import fileinput
import sys


def main():
    if len(sys.argv) < 2:
        print('''Usage: awpie 'prog' [file ...]''', file=sys.stderr)
        return 1

    prog = sys.argv[1]
    files = ['-']
    if len(sys.argv) >= 3:
        files = sys.argv[2:]

    for line in fileinput.input(files=files):
        line = line.strip('\r\n')
        exec(prog, None, {
            'line': line,
            'stdout': sys.stdout,
            'stderr': sys.stderr,
        })


if __name__ == '__main__':
    main()
