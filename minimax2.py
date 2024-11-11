# Initialize an empty board represented as a list with 9 spaces
board = [" " for x in range(9)]

# Function to print the current state of the board
def print_board():
    # Format each row of the board for display
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    # Print the board rows
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle a player's move
def player_move(icon):
    # Determine the player number based on the icon ("X" or "O")
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    # Prompt the player to enter a move
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    
    # Check if the chosen space is empty; if so, place the icon there
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        # If the space is taken, display an error message
        print()
        print("That space is already taken!")

# Function to check if a player has won
def is_victory(icon):
    # Check all possible winning combinations for the given icon
    if ((board[0] == icon and board[1] == icon and board[2] == icon) or 
        (board[3] == icon and board[4] == icon and board[5] == icon) or 
        (board[6] == icon and board[7] == icon and board[8] == icon) or 
        (board[0] == icon and board[3] == icon and board[6] == icon) or 
        (board[1] == icon and board[4] == icon and board[7] == icon) or 
        (board[2] == icon and board[5] == icon and board[8] == icon) or 
        (board[0] == icon and board[4] == icon and board[8] == icon) or 
        (board[2] == icon and board[4] == icon and board[6] == icon)):
        return True
    else:
        return False

# Function to check if the game is a draw
def is_draw():
    # If there are no empty spaces left on the board, it's a draw
    if " " not in board:
        return True
    else:
        return False

# Main game loop
while True:
    # Print the current board state
    print_board()
    
    # Player "X" makes a move
    player_move("X")
    
    # Print the board and check for victory or draw conditions for "X"
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

    # Player "O" makes a move
    player_move("O")
    
    # Print the board and check for victory or draw conditions for "O"
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
