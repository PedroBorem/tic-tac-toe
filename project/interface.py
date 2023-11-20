import customtkinter as ctk
import tkinter.messagebox
import joblib
import numpy as np
import pandas as pd

root = ctk.CTk()
root.title("Tic-Tac-Toe Model Checker")

def button_click(row, col):
    current_symbol = symbols[current_turn[0]]
    buttons[row][col].configure(text=current_symbol)
    current_turn[0] = (current_turn[0] + 1) % 2

def confirm_button_click():
    game_stage = [buttons[row][col].cget("text") for row in range(3) for col in range(3)]
    result = check_game_stage(game_stage)

    if result > 0:
        tkinter.messagebox.showinfo("Model Result", "X WINS !!!")
    else:
        tkinter.messagebox.showinfo("Model Result", "X LOSES !!!")

def check_game_stage(game_stage):

    game_stage_df = parse_game_to_df(game_stage)
    y_pred = model.predict(game_stage_df)

    return y_pred[0]

def parse_game_to_df(game_stage):
    mapped_values = [({'X': 1, 'O': -1, '': 0}[x]) for x in game_stage]

    game_stage_2d = np.array(mapped_values).reshape(1, -1)

    feature_names = [
        'Top-left-square', 'Top-middle-square', 'Top-right-square', 
        'Middle-left-square', 'Middle-middle-square', 'Middle-right-square', 
        'Bottom-left-square', 'Bottom-middle-square', 'Bottom-right-square'
    ]
    game_stage_df = pd.DataFrame(game_stage_2d, columns=feature_names)

    return game_stage_df

buttons = []
symbols = ['X', 'O']
current_turn = [0]
model = joblib.load(r'project\tic-tac-toe-model.joblib')

for row in range(3):
    button_row = []
    for col in range(3):
        button = ctk.CTkButton(root, text="", command=lambda row=row, col=col: button_click(row, col), width=280, height=280, font=("Helvetica", 124))
        button.grid(row=row, column=col, padx=10, pady=10)
        button_row.append(button)
    buttons.append(button_row)

confirm_button = ctk.CTkButton(root, text="Confirm", command=confirm_button_click)
confirm_button.grid(row=3, columnspan=3, pady=10)

root.mainloop()
