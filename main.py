from data import Data
from quiz_brain import QuizBrain
from ui import Quiz_UI

data = Data()
quiz = QuizBrain(data.questions)
ui = Quiz_UI(quiz)

