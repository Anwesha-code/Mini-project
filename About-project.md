3x3 Grid: The board is a 3x3 grid initialized with empty spaces.
Player Turns: Alternates between Player X and Player O.
Winner Check: Checks rows, columns, and diagonals for a winner.
Draw Check: Ends the game if the board is full and no winner is found.
Input Handling: Ensures valid row and column input (0-2) and checks if a cell is already occupied.


Game Logic
The game board is represented by a dictionary tic_tac_dic.
Players use symbols 'X' and 'O'.
The check_if_won function checks for winning conditions after each move.
In Player vs Bot mode, the bot makes random moves using the bots_move function.


Functions
get_player_input: Handles player input and updates the game board
display_game_board: Prints the current state of the game board
bots_move: Generates a random move for the bot
help_section: Displays game instructions
check_if_won: Checks if the current player has won
main: Main game loop
start: Initiates the game and handles game mode selection
