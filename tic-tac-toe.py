import numpy as np

# Function to check if the board is full
def is_board_full(board):
    return not any(' ' in row for row in board)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth+1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth+1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move using minimax
def find_best_move(board):
    best_score = -np.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*5)

# Main function to play the game
def play_tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    print("Let's play Tic Tac Toe!")
    print_board(board)
    while True:
        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        # AI's move
        print("AI's move:")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

# Start the game
play_tic_tac_toe()