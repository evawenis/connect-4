#!/usr/bin/env python3

import argparse

win = 4
vert = 6
hori = 7

def print_board(board):
    print('| ', end='')
    for i in range(1, len(board) + 1):
        print(f"{i}{'| ' if i < 9 else '|'}", end='')
    print()
    for i in reversed(range(len(board[0]))):
        print('|', end='')
        for j in range(len(board)):
            print(board[j][i], '|', end='')
        print()

def put(col, board, p):
    for i in range(len(board[0])):
        if board[col][i] == ' ':
            board[col][i] = p
            return col, i

    return -1, -1

def dig(board, j, v, i, h, cur):
    if not (0 <= j < hori and 0 <= i < vert) or cur != board[j][i]:
        return 0
    else:
        return 1 + dig(board, j + v, v, i + h, h, cur)

def judge(board, j, i):
    v = [-1, -1,  0, -1]
    h = [-1,  0, -1,  1]
    for k in range(len(v)):
        line = dig(board, j, v[k], i, h[k], board[j][i])
        line += dig(board, j, -v[k], i, -h[k], board[j][i]) - 1
        if line >= win:
            return True

    return False

def posint(num):
    try:
        num = int(num)
        if num < 0:
            raise argparse.ArgumentTypeError(f"Error: {num} should be positive integer")
        return num
    except:
        raise argparse.ArgumentTypeError(f"Error: {num} should be positive integer")

def main():
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--depth', help='depth, height, horizontal', type=posint)
    p.add_argument('-w', '--width', help='width', type=posint)
    p.add_argument('-l', '--win-line', help='win', type=posint)
    args = p.parse_args()

    global vert, hori, win
    if args.depth is not None:
        vert = int(args.depth)
    if args.width is not None:
        hori = int(args.width)
    if args.win_line is not None:
        win = int(args.win_line)
        if win > vert and win > hori:
            print("Error: win line is longer than width and height.")
            exit(1)

    board = [[' '] * vert for _ in range(hori)]

    turn = 1

    while turn <= vert * hori:
        print(f'Turn {turn}:')
        print_board(board)
        col = input('Type column\n> ')
        try:
            col = int(col) - 1
            if col < 0 or col > hori:
                print('Error: Type valid column number')
                continue
        except:
            continue

        p = 'o' if turn % 2 else 'x'
        j, i = put(col, board, p)
        if i == -1:
            print('Error: Already filled')
            continue
        if judge(board, j, i):
            print_board(board)
            print(f'{p} won!!!')
            return 0
        turn += 1

    print_board(board)
    print("draw")

if __name__ == '__main__':
    main()
