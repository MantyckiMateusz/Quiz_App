class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        '''A function that checks if there are still questions left'''
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        '''A function that returns the next question in the list formated as "question_number: question"'''
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question['question']}"
        

    def check_answer(self, user_answer) -> bool:
        '''A function checking whether user's answer matches the correct answer for current question'''
        correct_answer = self.current_question['answer']
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False


