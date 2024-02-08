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
