import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Main game window
window = tk.Tk()
window.title("Petals and Pitfalls")
window.geometry("700x700")

# Load images
board_img = Image.open(r"C:\Users\sriya\Downloads\Grid.jpg").resize((700, 700))
board_img = ImageTk.PhotoImage(board_img)

player1_img = Image.open(r"C:\Users\sriya\Downloads\player1.png").resize((30, 30))
player1_img = ImageTk.PhotoImage(player1_img)

player2_img = Image.open(r"C:\Users\sriya\Downloads\player2.png").resize((30, 30))
player2_img = ImageTk.PhotoImage(player2_img)

# Positions for ladders and snakes
ladders = {2: 38, 7: 12, 26: 78, 32: 55, 68: 91}
snakes = {33: 6, 45: 3, 73: 31, 94: 22, 98: 80}

# Player positions
player_positions = {"Player 1": 1, "Player 2": 1}
current_player = "Player 1"

# Function to switch to game screen
def start_game():
    welcome_frame.pack_forget()
    game_frame.pack()

# Function to roll dice and move player
def roll_dice():
    global current_player
    dice_roll = random.randint(1, 6)
    
    # Update player position
    player_positions[current_player] += dice_roll

    # Check for ladders and snakes
    if player_positions[current_player] in ladders:
        player_positions[current_player] = ladders[player_positions[current_player]]
    elif player_positions[current_player] in snakes:
        player_positions[current_player] = snakes[player_positions[current_player]]

    # Update player position on board
    update_board()

    # Check for winner
    if player_positions[current_player] >= 100:
        messagebox.showinfo("Game Over", f"{current_player} Wins!")
        reset_game()
    else:
        # Switch player
        current_player = "Player 1" if current_player == "Player 2" else "Player 2"
        update_turn_label()

# Function to update player tokens on board
def update_board():
    canvas.coords(player1_token, get_position_coords(player_positions["Player 1"]))
    canvas.coords(player2_token, get_position_coords(player_positions["Player 2"]))

# Function to get pixel coordinates for a given position
def get_position_coords(position):
    row = (position - 1) // 10
    col = (position - 1) % 10
    x = 50 + col * 60
    y = 600 - row * 60
    return x, y

# Function to reset game
def reset_game():
    global current_player
    player_positions["Player 1"] = 1
    player_positions["Player 2"] = 1
    current_player = "Player 1"
    update_board()
    update_turn_label()

# Function to update turn label
def update_turn_label():
    turn_label.config(text=f"{current_player}'s Turn")

# Welcome Screen
welcome_frame = tk.Frame(window)
welcome_frame.pack()

bg_label = tk.Label(welcome_frame, image=board_img)
bg_label.pack()

start_button = tk.Button(welcome_frame, text="Start Game", font=("Arial", 20), command=start_game)
start_button.place(relx=0.5, rely=0.8, anchor="center")

# Game Screen
game_frame = tk.Frame(window)

canvas = tk.Canvas(game_frame, width=700, height=700)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=board_img)

player1_token = canvas.create_image(*get_position_coords(1), image=player1_img)
player2_token = canvas.create_image(*get_position_coords(1), image=player2_img)

turn_label = tk.Label(game_frame, text="Player 1's Turn", font=("Arial", 20))
turn_label.pack()

roll_button = tk.Button(game_frame, text="Roll Dice", font=("Arial", 20), command=roll_dice)
roll_button.pack()

# Run the Tkinter main loop
window.mainloop()