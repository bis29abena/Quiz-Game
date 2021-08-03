class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def is_still_question(self):
        question = self.question_list
        if len(question) == self.question_number:
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You are right")
        else:
            print("You are wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
