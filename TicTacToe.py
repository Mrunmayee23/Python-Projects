from IPython.display import clear_output
def display_board(board) :
    clear_output()
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

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

