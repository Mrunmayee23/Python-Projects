from IPython.display import clear_output
import random 
def display_board(board) :
    clear_output()
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']

def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1: Enter your marker X or O: ").upper()
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark) 
    )

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else: 
        return 'Player 2'
