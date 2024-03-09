# awpie

![logo](https://i.ytimg.com/vi/M1Xlo4fLlJs/maxresdefault.jpg)

Using Python as awk alternative.

## Installation

```sh
$ pip install awpie
```

## Usage

Upper case all inputs:

```sh
$ printf 'apple\norange\n' | awpie 'print(line.upper())'
APPLE
ORANGE
```

Change orange to banana:

```sh
$ printf 'apple\norange\n' | awpie 'print(line) if line != "orange" else print("banana")'
apple
banana
```

## Command Line Options

```sh
$ awpie
Usage: awpie [--sep=separator] [--imports=module1,module2] [--begin='prog'] [--end='prog'] 'prog' [file ...]
```

### `sep`

Separator used to split a line, default value is blank.

### `imports`

Specify which modules will be imported before executing all codes. Can specify multiple modules like `--imports=csv,tomlib`.

These modules are imported by default:

- collections
- fileinput
- functools
- getopt
- importlib
- itertools
- operator
- os
- sys

### `begin`

Codes that will be executed before processing all files.

### `end`

Codes that will be executed after processing all files.

### `prog`

Codes that will be executed for every line.

### `file`

File to process. Default is to read a stream from `stdin` as the file.

## Local variables

| Name          | Type        | Description                                                            |
| ------------- |------------ | ---------------------------------------------------------------------- |
| `line`        | `str`       | Current line.                                                          |
| `fields`      | `list[str]` | Result of `line.split(sep)`. `sep` can be specified in arguments.      |
| `data`        | `dict`      | An empty dict, can be used to store custom values.                     |
| `stdout`      |             | `sys.stdout`.                                                          |
| `stderr`      |             | `sys.stderr`.                                                          |
| `filename`    | `str`       | Name of the file currently being read.                                 |
| `fileno`      | `int`       | File descriptor for the current file.                                  |
| `lineno`      | `int`       | Cumulative line number of the line that has just been read.            |
| `filelineno`  | `int`       | Line number in the current file.                                       |
| `isfirstline` | `bool`      | Whether the line just read is the first line of its file or not.       |
| `isstdin`     | `bool`      | Whether the last line was read from sys.stdin or not.                  |
| `nextfile`    | `callable`  | Close current file so that next iteration will be read from next file. |
| `close`       | `callable`  | Close the sequence.                                                    |
