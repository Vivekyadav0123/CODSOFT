
# Tic Tac Toe Game with AI (Minimax Algorithm)

import math

# Welcome message
print("Welcome to Tic Tac Toe!")
print("You are X (Player), and AI is O")

# Initialize empty board
board = [" " for _ in range(9)]

# Display the board in 3x3 grid
def print_board():
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")

# Get valid move from the player
def player_move():
    while True:
        try:
            move = int(input("Your move (1–9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is taken or invalid. Try again.")
        except:
            print("Please enter a number between 1 and 9.")

# Check if someone has won or if it’s a draw
def check_winner(brd):
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],    # rows
        [0,3,6],[1,4,7],[2,5,8],    # columns
        [0,4,8],[2,4,6]             # diagonals
    ]
    for a, b, c in win_patterns:
        if brd[a] == brd[b] == brd[c] != " ":
            return brd[a]
    if " " not in brd:
        return "draw"
    return None

# Minimax algorithm for AI
def minimax(brd, is_max):
    winner = check_winner(brd)
    if winner == "O": return 1
    if winner == "X": return -1
    if winner == "draw": return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, False)
                brd[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, True)
                brd[i] = " "
                best = min(best, score)
        return best

# AI selects best move
def ai_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# Main game function
def play_game():
    print_board()
    while True:
        player_move()
        print_board()
        outcome = check_winner(board)
        if outcome:
            break

        print("\nAI is thinking...\n")
        ai_move()
        print_board()
        outcome = check_winner(board)
        if outcome:
            break

    # Final result
    print("\nGame Over!")
    if outcome == "draw":
        print("It's a draw.")
    elif outcome == "X":
        print("You win!")
    else:
        print("AI wins. Better luck next time.")

# Start the game
play_game()
