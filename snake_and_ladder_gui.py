# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:17:16 2025

@author: adars
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Constants
END = 100

# Snake and Ladder positions
LADDERS = {
    8: 26,
    21: 82,
    43: 77,
    50: 91,
    54: 93,
    62: 96,
    66: 87,
    80: 100
}

SNAKES = {
    44: 22,
    46: 9,
    48: 7,
    52: 11,
    55: 7,
    59: 17,
    64: 36,
    69: 33,
    73: 1,
    83: 19,
    92: 51,
    95: 24,
    98: 28
}

class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder Game")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.pp1_name = ""
        self.pp2_name = ""
        self.pp1 = 0
        self.pp2 = 0
        self.turn = 0

        self.create_widgets()

    def create_widgets(self):
        """Create the game board and widgets"""
        
        # Game board image
        self.board_img = Image.open("slb.jpg")
        self.board_img = self.board_img.resize((400, 400))
        self.board_photo = ImageTk.PhotoImage(self.board_img)
        self.board_label = tk.Label(self.root, image=self.board_photo)
        self.board_label.grid(row=0, column=0, columnspan=4)

        # Player info
        self.pp1_label = tk.Label(self.root, text="Player 1: ", font=("Helvetica", 14))
        self.pp1_label.grid(row=1, column=0, sticky="w")
        self.pp2_label = tk.Label(self.root, text="Player 2: ", font=("Helvetica", 14))
        self.pp2_label.grid(row=2, column=0, sticky="w")

        # Buttons
        self.roll_button = tk.Button(self.root, text="Roll Dice", font=("Helvetica", 14), command=self.roll_dice)
        self.roll_button.grid(row=3, column=0, columnspan=2)
        
        self.quit_button = tk.Button(self.root, text="Quit Game", font=("Helvetica", 14), command=self.quit_game)
        self.quit_button.grid(row=3, column=2, columnspan=2)

        # Display Player positions
        self.pp1_pos_label = tk.Label(self.root, text="Position: 0", font=("Helvetica", 14))
        self.pp1_pos_label.grid(row=1, column=1)
        
        self.pp2_pos_label = tk.Label(self.root, text="Position: 0", font=("Helvetica", 14))
        self.pp2_pos_label.grid(row=2, column=1)

        self.status_label = tk.Label(self.root, text="Welcome to Snake and Ladder!", font=("Helvetica", 16), fg="green")
        self.status_label.grid(row=4, column=0, columnspan=4)

        # Start game dialog
        self.start_game()

    def start_game(self):
        """Prompt for player names and start the game"""
        def start():
            self.pp1_name = pp1_name_entry.get()
            self.pp2_name = pp2_name_entry.get()
            if self.pp1_name and self.pp2_name:
                self.pp1_label.config(text=f"Player 1: {self.pp1_name}")
                self.pp2_label.config(text=f"Player 2: {self.pp2_name}")
                self.pp1_pos_label.config(text="Position: 0")
                self.pp2_pos_label.config(text="Position: 0")
                self.status_label.config(text=f"{self.pp1_name}'s turn!")
                game_start_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter names for both players.")

        game_start_window = tk.Toplevel(self.root)
        game_start_window.title("Enter Player Names")
        
        tk.Label(game_start_window, text="Player 1 Name:").grid(row=0, column=0)
        pp1_name_entry = tk.Entry(game_start_window)
        pp1_name_entry.grid(row=0, column=1)
        
        tk.Label(game_start_window, text="Player 2 Name:").grid(row=1, column=0)
        pp2_name_entry = tk.Entry(game_start_window)
        pp2_name_entry.grid(row=1, column=1)
        
        tk.Button(game_start_window, text="Start", command=start).grid(row=2, column=0, columnspan=2)

    def roll_dice(self):
        """Handle dice roll and player movement"""
        if self.turn % 2 == 0:
            player_name = self.pp1_name
            player_position = self.pp1
        else:
            player_name = self.pp2_name
            player_position = self.pp2

        dice = random.randint(1, 6)
        player_position += dice
        player_position = self.check_ladder(player_position)
        player_position = self.check_snake(player_position)

        if player_position > END:
            player_position = END
        
        # Update positions and turn
        if self.turn % 2 == 0:
            self.pp1 = player_position
            self.pp1_pos_label.config(text=f"Position: {self.pp1}")
        else:
            self.pp2 = player_position
            self.pp2_pos_label.config(text=f"Position: {self.pp2}")

        # Check if the player has won
        if player_position == END:
            self.status_label.config(text=f"{player_name} wins!")
            self.roll_button.config(state="disabled")
            self.quit_button.config(state="disabled")
        else:
            self.turn += 1
            next_player = self.pp2_name if self.turn % 2 == 0 else self.pp1_name
            self.status_label.config(text=f"{next_player}'s turn!")

    def check_ladder(self, position):
        """Check for ladder and update position"""
        return LADDERS.get(position, position)

    def check_snake(self, position):
        """Check for snake and update position"""
        return SNAKES.get(position, position)

    def quit_game(self):
        """Quit the game"""
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
