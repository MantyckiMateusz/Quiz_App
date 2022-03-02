from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz_UI:
    def __init__(self, quiz: QuizBrain):
        #Get main quiz functionality from QuizBrain object
        self.quiz = quiz

        #Create a window
        self.window = Tk()
        self.window.title('Quiz app')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

       #Create a canvas with question text
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150, 
            125,
            text='test',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR,
            width=280
            )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #Create score counter
        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        #Create True and False buttons
        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_img, border=0, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, border=0, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)
        
        #Get first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        '''A function that changes the canvas text to a new question as long as there are questions left in the list'''
        #Change bg color back to white in case it was changed in one of the answer functions
        self.canvas.config(bg='white')
        #If there are still questions left display next question, else disable buttons and notify the user that he reached the end of the quiz
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def answer_true(self):
        '''A function activated by clicking True button it calls the QuizBrain.check_answer function and flashes canvas green if it returned true else it flashes red.'''
        if self.quiz.check_answer('True'):
            self.flash_green()
        else:
            self.flash_red()
        self.update_score()
    
    def answer_false(self):
        '''A function activated by clicking False button it calls the QuizBrain.check_answer function and flashes canvas green if it returned true else it flashes red.'''
        if self.quiz.check_answer('False'):
            self.flash_green()
        else:
            self.flash_red()
        self.update_score()

    def update_score(self):
        '''A function that updated text in score label'''
        self.score_label['text'] = f'Score: {self.quiz.score}'

    def flash_green(self):
        '''A function that flashes canvas green for 1 second'''
        self.canvas.config(bg='green')
        self.window.after(1000, func=self.get_next_question)

    def flash_red(self):
        '''A function that flashes canvas red for 1 second'''
        self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)