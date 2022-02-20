# A Simple Beginner Project.
# x -> Player
# O -> CPU
import random

board = [' ' for x in range(10)]


def letter_insert(l, pos):
    board[pos] = l


def free_space(pos) -> bool:
    return (board[pos] == ' ')


def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(board, l):
    return (
        (board[7] == l and board[8] == l and board[9] == l) or  # bottom row 
        (board[4] == l and board[5] == l and board[6] == l) or  # middle row
        (board[1] == l and board[2] == l and board[3] == l) or  # top row
        (board[1] == l and board[4] == l and board[7] == l) or  # first column
        (board[2] == l and board[5] == l and board[8] == l) or  # second column
        (board[3] == l and board[6] == l and board[9] == l) or  # third column
        (board[1] == l and board[5] == l and board[9] == l) or  # diagonal-1
        (board[3] == l and board[5] == l and board[7] == l))  # diagonal-2


def board_full(board) -> bool:
    if board.count(' ') > 1:
        return False
    else:
        return True


def player_move():
    run = True
    while run:
        move = input('Select a Position (1-9): ')

        try:
            move = int(move)
            if move > 0 and move < 10:
                if (free_space(move)):
                    run = False
                    letter_insert('X', move)
                else:
                    print('Chosen space occupied. Select another one.')
            else:
                print('Enter a number between the specififed range.')
        except:
            print('Type a number.')


def cpu_move():
    moves_possible = [x for x, l in enumerate(board) if l == ' ' and x != 0]
    move = 0

    # checks if it's possible for either the CPU or Player to win at some position
    for a in ['O', 'X']:
        for i in moves_possible:
            copy_board = board[:]
            copy_board[i] = a
            if is_winner(copy_board, a):
                move = i
                return move

    # checking any available open corners
    open_corners = []
    for i in moves_possible:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    if len(open_corners) > 0:
        move = random.choice(open_corners)
        return move

    # checks if the middle position is up for grabs
    if 5 in moves_possible:
        move = 5
        return move

    # checking any available open corners
    open_edges = []
    for i in moves_possible:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)
    if len(open_edges) > 0:
        move = random.choice(open_edges)
        return move

    return move


def main():
    print('Tic-Tac-Toe: ')
    print_board(board)

    while not (board_full(board)):
        if not (is_winner(board, 'O')): # Player's Move
            player_move()
            print_board(board)
        else:
            print('CPU Won!')
            break

        if not (is_winner(board, 'X')): # CPU's move
            move = cpu_move()
            if move == 0: # If CPU couldn't find a place to move.
                print("Game's a Tie.")
            else:
                letter_insert('O', move)
                print("CPU placed an 'O' at position ", move, ':')
                print_board(board)
        else:
            print('You Won!')
            break

    if (board_full(board)):
        print("Game's a Tie.")


if __name__ == '__main__':
    main()