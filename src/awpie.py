import fileinput
import sys


def main():
    if len(sys.argv) >= 2:
        prog = sys.argv[1]
    else:
        prog = """Usage: awpie 'prog' [file ...]"""

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
