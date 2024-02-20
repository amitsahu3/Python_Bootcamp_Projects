import tkinter
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizzInterface:
    def __init__(self, quiz_brain:QuizBrain):           # quiz_brain must be of QuizBrain data type
        self.quiz = quiz_brain

        # setting the window
        self.window = Tk()
        self.window.title("Quizzeler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=10)

        self.score_label = Label(text='Score:0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)


        # setting the canvas
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='hi', font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # setting the true/false button
        true_image = PhotoImage(file='images/true.png')     # 'C:/Users/nitro/Desktop/PythonBootCamp/day-34(quizzler app)/images/true.png'
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')  # reset the canvas
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'Quizz Ended \n Your final score is {self.quiz.score}')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_clicked(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)


    # to change canvas color to red if wrong and white if right after certain seconds
    # cant use time with mainloop as mainloop keeps on running by side
    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
