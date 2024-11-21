def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to 3x3 Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        try:
            row, col = map(int, input("Enter your move (row and column, 0-2) separated by space: ").split())
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")
            continue

        board[row][col] = current_player
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

