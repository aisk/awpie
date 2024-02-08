# awpie

![logo](https://cdn.epiccarry.com/wp-content/uploads/sites/31/2023/11/cs2-subtick-1.webp)

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
