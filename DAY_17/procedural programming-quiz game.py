from data_file1 import question_data

score = 0
question_number = 0


def get_question():
    global question_number
    if question_number < len(question_data):
        return question_number
    return None


def check_answer(user_answer, correct_answer):
    global score
    if user_answer == correct_answer:
        score += 1
        print("You got it right!")
    else:
        print(f"You got that wrong!")


game = True
while game:
    question_index = get_question()
    if question_index is not None:
        question_text = question_data[question_index]["text"]
        guess = input(f"Q{question_index + 1}: {question_text} (True/False): ").lower()
        question_answer = question_data[question_index]["answer"]

        question_number += 1

        check_answer(guess, question_answer.lower())

        print(f"Your Score is {score}/{question_number}")
        print(f"The correct answer was {question_answer}.")
        print("\n")

    else:
        game = False

print("You have completed the quiz! Congratulations.")
print(f"Your final score was {score}/{question_number}")
