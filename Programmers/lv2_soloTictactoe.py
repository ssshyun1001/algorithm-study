# Problem: Solo Tic-tac-toe
# Platform: Programmers
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/160585
# Level: Lv.2

# Approach:
# - Count the number of O's and X's on the board.
# - Check whether the number of turns is valid:
#   O always goes first, so the number of O's must be equal to
#   the number of X's or exactly one more.

# - Check whether O or X has a winning line
#   (row, column, or diagonal).

# - Validate the board based on the winning condition:
#   - If both O and X win, the board is invalid.
#   - If O wins, O must have exactly one more move than X.
#   - If X wins, O and X must have the same number of moves.
# - If none of the invalid conditions apply, return 1.

def solution(board):
    # Count O and X
    count_O = 0
    count_X = 0

    for i in range(3):
        count_O += board[i].count('O')
        count_X += board[i].count('X')

    # O always starts first
    if not (count_O == count_X or count_O == count_X + 1):
        return 0

    o_win = False
    x_win = False

    # Check rows and columns
    for i in range(3):
        # row
        if board[i][0] != '.' and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            if board[i][0] == 'O':
                o_win = True
            else:
                x_win = True

        # column
        if board[0][i] != '.' and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            if board[0][i] == 'O':
                o_win = True
            else:
                x_win = True

    # Check diagonals
    if board[1][1] != '.' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[1][1] == 'O':
            o_win = True
        else:
            x_win = True

    if board[1][1] != '.' and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        if board[1][1] == 'O':
            o_win = True
        else:
            x_win = True

    # Both players cannot win at the same time
    if o_win and x_win:
        return 0

    # If O wins, O must have one more move than X
    if o_win and count_O != count_X + 1:
        return 0

    # If X wins, O and X must have the same number of moves
    if x_win and count_O != count_X:
        return 0

    return 1