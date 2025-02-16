import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

#welcome game window
window = tk.Tk() #create a window
welcome_img = Image.open("images/IMG_0136.jpeg").resize((700, 700))
welcome_img = ImageTk.PhotoImage(welcome_img) #convert image for tkinter
window.welcome_img = welcome_img  #keep reference to image
label = tk.Label(window, image=welcome_img) #create a label with the image
label.pack() # show the label
window.title("Petals and Perils") #set the title of the window
window.geometry("700x700") #set the size of the window



#load button for playing game
play_button_path = "images/IMG_0137.jpeg"  
play_button_img = Image.open(play_button_path).resize((350, 100)) 
#resize the button so that it alligns with the text

#convert the image for tkinter
play_button_img = ImageTk.PhotoImage(play_button_img)

# Function to calculate x and y coordinates for each box in the grid
def get_coordinates():
    grid_size = 10
    screen_width = 1000
    screen_height = 1000
   
    # Calculate the width and height for each box
    box_width = screen_width / grid_size  # 100px per box horizontally
    box_height = screen_height / grid_size  # 100px per box vertically
   
    coordinates = []
   
    # Loop through each grid number from 1 to 100
    for num in range(1, grid_size * grid_size + 1):
        row = (num - 1) // grid_size  # Calculate row (0-indexed)
        col = (num - 1) % grid_size  # Calculate column (0-indexed)
       
        # Alternate the direction of the x-coordinate (snake-like pattern)
        if row % 2 == 0:  # If the row is even (starting from the bottom)
            x = col * box_width
        else:  # If the row is odd
            x = (grid_size - col - 1) * box_width
       
        # Calculate y-coordinate (increasing from bottom to top)
        y = (grid_size - row - 1) * box_height
       
        # Append the coordinates
        coordinates.append((num, x, y))
   
    return coordinates

# Get the coordinates for the 10x10 grid
coordinates = get_coordinates()


#function to handle button click
def play_game():
    game_window = tk.Toplevel(window)  #new window with board
    board_img = Image.open("images/IMG_0140.jpeg").resize((1000, 900))
    game_window.title("Game Board")
    game_window.geometry("1000x1000") 
    board_img = ImageTk.PhotoImage(board_img)
    label = tk.Label(game_window, image=board_img)
    label.pack()
    
    #add the player images
    player1_img = Image.open("images/sprout1.png").resize((50, 50))
    player1_img = ImageTk.PhotoImage(player1_img)
    player2_img = Image.open("images/sprout2.png").resize((50, 50))
    player2_img = ImageTk.PhotoImage(player2_img)
    
 # Add the player tokens to the board
    player1_token = tk.Label(game_window, image=player1_img)
    player1_token.place(x=30, y=775)  # Place player1 at specific coordinates
    player2_token = tk.Label(game_window, image=player2_img)
    player2_token.place(x=80, y=775)  # Place player2 at specific coordinates
    
# Keep references to the images to prevent them from being garbage collected
    game_window.player1_img = player1_img
    game_window.player2_img = player2_img
    game_window.board_img = board_img
    

    game_window.mainloop()
    
    
    
    


   
    #board_label = tk.Label(game_window, text="Game Board", font=("Arial", 24))
    #board_label.pack(pady=20)

    # Example: Adding a canvas for a game board
    #board_canvas = tk.Canvas(game_window, width=800, height=800, bg="white")
    #board_canvas.pack(pady=20)

#create the play button
play_button = tk.Button(
    window, image=play_button_img, borderwidth=0, highlightthickness=0, command=play_game
)

#place the button at the "Play Game" text location
play_button.place(x=200, y=560)  

# Keep references to the images to prevent garbage collection
window.welcome_img = welcome_img
window.play_button_img = play_button_img



# Load images
#board_img = Image.open(r"C:\Users\sriya\Downloads\Grid.jpg").resize((700, 700))
#board_img = ImageTk.PhotoImage(board_img)

#player1_img = Image.open(r"C:\Users\sriya\Downloads\player1.png").resize((30, 30))
#player1_img = ImageTk.PhotoImage(player1_img)

#player2_img = Image.open(r"C:\Users\sriya\Downloads\player2.png").resize((30, 30))
#player2_img = ImageTk.PhotoImage(player2_img)

# Positions for ladders and snakes
#ladders = {2: 38, 7: 12, 26: 78, 32: 55, 68: 91}
#snakes = {33: 6, 45: 3, 73: 31, 94: 22, 98: 80}

# Player positions
#player_positions = {"Player 1": 1, "Player 2": 1}
#current_player = "Player 1"

# Function to switch to game screen
#def start_game():
    #welcome_frame.pack_forget()
    #game_frame.pack()

# Function to roll dice and move player
#def roll_dice():
    #global current_player
    #dice_roll = random.randint(1, 6)
    
    # Update player position
    #player_positions[current_player] += dice_roll

    # Check for ladders and snakes
    #if player_positions[current_player] in ladders:
       # player_positions[current_player] = ladders[player_positions[current_player]]
    #elif player_positions[current_player] in snakes:
       # player_positions[current_player] = snakes[player_positions[current_player]]

    # Update player position on board
    #update_board()

    # Check for winner
    #if player_positions[current_player] >= 100:
       # messagebox.showinfo("Game Over", f"{current_player} Wins!")
        #reset_game()
    #else:
        # Switch player
        #current_player = "Player 1" if current_player == "Player 2" else "Player 2"
        #update_turn_label()

# Function to update player tokens on board
#def update_board():
    #canvas.coords(player1_token, get_position_coords(player_positions["Player 1"]))
    #canvas.coords(player2_token, get_position_coords(player_positions["Player 2"]))

# Function to get pixel coordinates for a given position
#def get_position_coords(position):
    #row = (position - 1) // 10
    #col = (position - 1) % 10
    #x = 50 + col * 60
    #y = 600 - row * 60
    #return x, y

# Function to reset game
#def reset_game():
    #global current_player
    #player_positions["Player 1"] = 1
    #player_positions["Player 2"] = 1
    #current_player = "Player 1"
    #update_board()
    #update_turn_label()

# Function to update turn label
#def update_turn_label():
    #turn_label.config(text=f"{current_player}'s Turn")

# Welcome Screen
#welcome_frame = tk.Frame(window)
#welcome_frame.pack()

#bg_label = tk.Label(welcome_frame, image=board_img)
#bg_label.pack()

#start_button = tk.Button(welcome_frame, text="Start Game", font=("Arial", 20), command=start_game)
#start_button.place(relx=0.5, rely=0.8, anchor="center")

# Game Screen
#game_frame = tk.Frame(window)

#canvas = tk.Canvas(game_frame, width=700, height=700)
#canvas.pack()
#canvas.create_image(0, 0, anchor="nw", image=board_img)

#player1_token = canvas.create_image(*get_position_coords(1), image=player1_img)
#player2_token = canvas.create_image(*get_position_coords(1), image=player2_img)

#turn_label = tk.Label(game_frame, text="Player 1's Turn", font=("Arial", 20))
#turn_label.pack()

#roll_button = tk.Button(game_frame, text="Roll Dice", font=("Arial", 20), command=roll_dice)
#roll_button.pack()

# Run the Tkinter main loop
window.mainloop()