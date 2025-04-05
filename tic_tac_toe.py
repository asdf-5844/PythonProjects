"""
This program simulates the game of tic tac toe.
"""

# get_valid_index
# -----
# Get row or column from user
def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if 0 <= index <= 2:
                return index
            print("Must be 0 - 2 inclusive!")
        except ValueError:
            print("Must be an integer!")

# game_is_over
# -----
# Return True if the game is over and False
# otherwise. Print a message indicating who
# won or whether there was a tie.
def game_is_over(board):
    for i in range(3):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            print_board(board)
            print(board[i][0] + " wins!")
            return True
        
        # Check vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            print_board(board)
            print(board[0][i] + " wins!")
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        print_board(board)
        print(board[0][0] + " wins!")
        return True
    
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        print_board(board)
        print(board[2][0] + " wins!")
        return True
    
    # Check tie
    if all(" " not in row for row in board):
        print_board(board)
        print("Tie game!")
        return True
    
    # Not over yet!
    return False
    
# print_board
# -----
# Print the board.
def print_board(board):
    for row in board:
        print(row)

# Set up board
# This part creates a list with 3 space characters, like [" ", " ", " "].
board = [[" " for _ in range(3)] for _ in range(3)]

# x goes first
turn = "x"

# Play tic tac toe
while not game_is_over(board):
    print_board(board)
    print("It's " + turn + "'s turn.")
    row = get_valid_index("Row: ")
    col = get_valid_index("Col: ")
    
    # Check if the selected space is empty
    if board[row][col] != " ":
        print("That space is already taken. Try again.")
        continue
    
    # Place the player's move on the board
    board[row][col] = turn
    
    # Switch turn
    turn = "o" if turn == "x" else "x"
