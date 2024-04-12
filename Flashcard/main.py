# importing modules
from tkinter import *
import pandas
import random



FONT = ('Ariel', 40, 'italic')
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# function to get french word and their translation
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')        # if not found then use original data(not run even once)
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    # every time we go to a new card we invalidate this timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)

    # create a new timer again
    flip_timer = window.after(5000, func=flip_card)

# function to flip the card

def flip_card():
    canvas.itemconfig(card_title, text='English' )
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(card_background, images=card_back_img)

# is known fun to remove current card from to learn dict
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()





window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# after creating the window , create timer to flip the card
flip_timer = window.after(5000, func=flip_card)

# creating the canvas
canvas =  Canvas(width=800, height=526)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400,263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=FONT)
card_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'italic'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, padx=20, pady=20, columnspan=2)

# cross button
cross_img = PhotoImage(file='./images/wrong.png')
cross_button = Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

# check button
check_img = PhotoImage(file='./images/right.png')
check_button = Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

# calling the function at the last
next_card()
window.mainloop()


