from question_model import Question

# Within the question_model, A Question class was created containing two attributes "Text" and "Answers"

from data import question_data

# Within the question_data there are lists of questions and answers
# embedded within a dictionary

question_bank = []

from quiz_brain import QuizBrain

#Within the quiz_brain class we have 3 attributes and 3 methods
# The still_have_question method ensures the while loop runs while there are questions yet unanswered
# The next_question method ensures that the questions within the question banks are asked within a sequential order
# The check_answer method compares the user response with the correct response


for x in question_data:
    q_text = x['text']
    q_answer = x['answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)
    # new_question is an object as denoted by the Question class
    # And we are appending this new_question to an empty list
    # The question_bank now contains 12 list of objects with questions and answers

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print('You have completed the Quiz')
print(f"Your final score was {quiz.score}/{quiz.question_number}")