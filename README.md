# connect4.py

## usage

```sh
$ python3 connect4.py
Turn 1:
| 1| 2| 3| 4| 5| 6| 7|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
Type column
> 4
Turn 2:
| 1| 2| 3| 4| 5| 6| 7|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |o |  |  |  |
Type column
> 5
Turn 3:
| 1| 2| 3| 4| 5| 6| 7|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |o |x |  |  |
Type column
>
...
```

## help

```sh
$ ./connect4.py --help
usage: connect4.py [-h] [-d DEPTH] [-w WIDTH] [-l WIN_LINE] [-e]

optional arguments:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        depth, height, horizontal
  -w WIDTH, --width WIDTH
                        width
  -l WIN_LINE, --win-line WIN_LINE
                        win
  -e, --extended        enable the way to specify column by qwerty
```

