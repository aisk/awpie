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

## Local variables

| Name          | Description                                                            |
| ------------- | ---------------------------------------------------------------------- |
| `line`        | Current line.                                                          |
| `fields`      | Result of `line.split(sep)`. `sep` can be specified in arguments.      |
| `data`        | An empty dict, can be used to store custom values.                     |
| `stdout`      | `sys.stdout`.                                                          |
| `stderr`      | `sys.stderr`.                                                          |
| `filename`    | Name of the file currently being read.                                 |
| `fileno`      | File descriptor for the current file.                                  |
| `lineno`      | Cumulative line number of the line that has just been read.            |
| `filelineno`  | Line number in the current file.                                       |
| `isfirstline` | Whether the line just read is the first line of its file or not.       |
| `isstdin`     | Whether the last line was read from sys.stdin or not.                  |
| `nextfile`    | Close current file so that next iteration will be read from next file. |
| `close`       | Close the sequence.                                                    |
