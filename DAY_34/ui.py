from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizzler: QuizBrain):
        self.quiz = quizzler

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.time_id = None

        self.game_score = Label(bg=THEME_COLOR, fg="white")
        self.game_score.grid(padx=20, pady=20, column=2, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.word_text = self.canvas.create_text(150, 125, width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(padx=20, pady=20, column=0, row=1, columnspan=3)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, command=self.true_pressed)
        self.true_button.grid(padx=20, pady=20, column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, command=self.false_pressed)
        self.false_button.grid(padx=20, pady=20, column=2, row=2)

        self.get_score()
        self.get_question()

        self.window.mainloop()

    def get_score(self):
        score = self.quiz.score
        self.game_score.config(text=f"Score: {score}")

    def get_question(self):
        if self.time_id is not None:
            self.window.after_cancel(self.time_id)

        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.get_score()
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.word_text, text=question)
            self.true_button.config(state="active")
            self.false_button.config(state="active")
        else:
            self.get_score()
            self.canvas.itemconfig(self.word_text,
                                   text="You've completed the quiz!\n"
                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        user_answer = "True"
        self.get_feedback(self.quiz.check_answer(user_answer))

    def false_pressed(self):
        user_answer = "False"
        self.get_feedback(self.quiz.check_answer(user_answer))

    def get_feedback(self, user_input):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if user_input:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.time_id = self.window.after(1000, self.get_question)
