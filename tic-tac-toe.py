import tkinter as tk
import random

# Define the game board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define the AI player
AI_PLAYER = "X"
HUMAN_PLAYER = "O"


def get_empty_cells(board):
    """Get the list of empty cells on the board"""
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells


def check_win(board, player):
    """Check if the specified player has won"""
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def ai_move():
    """Make a move for the AI player"""
    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return
    i, j = random.choice(empty_cells)
    board[i][j] = AI_PLAYER
    update_board()


def human_move(i, j):
    """Make a move for the human player"""
    if board[i][j] != " ":
        return
    board[i][j] = HUMAN_PLAYER
    update_board()
    ai_move()


def update_board():
    """Update the GUI with the current state of the board"""
    for i in range(3):
        for j in range(3):
            button = buttons[i][j]
            button.config(text=board[i][j])
            button.config(state=tk.DISABLED if board[i][j] != " " else tk.NORMAL)
    if check_win(board, HUMAN_PLAYER):
        status_label.config(text="You win!")
        disable_buttons()
    elif check_win(board, AI_PLAYER):
        status_label.config(text="AI wins!")
        disable_buttons()
    elif not get_empty_cells(board):
        status_label.config(text="Tie!")
        disable_buttons()


def disable_buttons():
    """Disable all the buttons on the board"""
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)


# Create the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 32), width=3, height=1,
                           command=lambda i=i, j=j: human_move(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)

# Start the game
ai_move()

root.mainloop()
