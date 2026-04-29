from tkinter import *
import pandas
import random

# ---------------------------- FRENCH CARD ------------------------------- #
try:
    new_data = pandas.read_csv("data/words_to_learn.csv")
    dataset = new_data.to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    old_data = pandas.read_csv("data/french_words.csv")
    dataset = old_data.to_dict(orient="records")

current_word = ""
time_id = None


def next_card():
    if dataset:
        global current_word
        current_word = random.choice(dataset)
        word = current_word["French"]
        canvas.itemconfig(photo_image, image=card_front_image)
        canvas.itemconfig(title_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=word, fill="black")
        if time_id is not None:
            window.after_cancel(time_id)
        countdown()
    else:
        if time_id is not None:
            window.after_cancel(time_id)
        canvas.itemconfig(title_text, text="Completed", fill="black")
        canvas.itemconfig(word_text, text="Well-Done!", fill="black")


# ---------------------------- ENGLISH CARD ------------------------------- #
def flip_card():
    global current_word
    word = current_word["English"]
    canvas.itemconfig(photo_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word, fill="white")


# ---------------------------- MEMORISED CARD ------------------------------- #
def known_card():
    global time_id
    if time_id is not None:
        window.after_cancel(time_id)
    if not dataset:
        canvas.itemconfig(title_text, text="Completed", fill="black")
        canvas.itemconfig(word_text, text="Well-Done!", fill="black")
        return
    global current_word
    dataset.remove(current_word)
    new_dataset = pandas.DataFrame(dataset)
    new_dataset.to_csv("data/words_to_learn.csv", index=0)
    next_card()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown():
    global time_id
    time_id = window.after(3000, flip_card)


# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
photo_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
next_card()
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_card)
right_button.grid(column=1, row=1)

window.mainloop()
