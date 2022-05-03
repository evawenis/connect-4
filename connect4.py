#!/usr/bin/env python3

def print_board(board):
    num = [str(i) for i in range(1, len(board) + 1)]
    print('|' + ' |'.join(num) + ' |')
    for i in reversed(range(len(board[0]))):
        print('|', end='')
        for j in range(len(board)):
            print(board[j][i], '|', end='')
        print()

def put(col, board, p):
    print(col)
    for i in range(len(board[0])):
        if board[col][i] == ' ':
            board[col][i] = p
            return True

    return False

ud = [0, 1, 1, 1, 0, -1, -1, -1]
lr = [-1, -1, 0, 1, 1, 1, 0, -1]
def dig(board, v, h, index, cur):
    if not (0 <= v <= 5 and 0 <= h <= 6):
        return 0
    elif cur != board[h][v]:
        return 0
    return 1 + dig(board, v + ud[index], h + lr[index], index, cur)

def judge(board):
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] != ' ':
                cur = board[j][i]
                count = 1
                for k in range(len(ud)):
                    v = i + ud[k]
                    h = j + lr[k]
                    if 0 <= v <= 5 and 0 <= h <= 6:
                        if cur == board[h][v]:
                            if dig(board, v, h, k, cur) == 3:
                                return True
    return False

def main():
    board = [[' '] * 6 for _ in range(7)]

    turn = 1

    while True:
        print(f'Turn {turn}:')
        print_board(board)
        col = input('Type column\n> ')
        try:
            col = int(col) - 1
            if col < 0 or col > 6:
                print('Error: Type valid column number')
                continue
        except:
            continue

        p = 'o' if turn % 2 else 'x'
        if not put(col, board, p):
            print('Error: Already filled')
            continue
        if judge(board):
            print_board(board)
            print(f'{p} won!!!')
            break
        turn += 1

if __name__ == '__main__':
    main()
