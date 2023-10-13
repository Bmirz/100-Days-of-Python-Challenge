# Imports 
from tkinter import *
import pandas
import random

# Constant Variables
BACKGROUND_COLOR = "#B1DDC6"
to_learn = None
current_card = None


try:
    data = pandas.read_csv("day031/FlashCardProject/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day031/FlashCardProject/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- NEW CARD ------------------------------- #

def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer) #NOTE: Restart flip timer

    print(current_card)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, func=flip_card) #NOTE: After 3 seconds, flip card

# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

# ---------------------------- IS KNOWN ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("day031/FlashCardProject/data/words_to_learn.csv", index=False)

    next_card()

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) #NOTE: After 3 seconds, flip card

# Images
card_back_img = PhotoImage(file="day031/FlashCardProject/images/card_back.png")
card_front_img = PhotoImage(file="day031/FlashCardProject/images/card_front.png")
right_img = PhotoImage(file="day031/FlashCardProject/images/right.png")
wrong_img = PhotoImage(file="day031/FlashCardProject/images/wrong.png")

# Canvas
canvas = Canvas(height=526, width=800, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 264, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="",font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="",font=("Ariel", 60, "bold"))

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1, columnspan=2)

next_card()

window.mainloop()