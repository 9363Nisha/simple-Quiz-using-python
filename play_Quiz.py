questions = [
    {
    'prompt': 'What is the output of print(5/2) in Python?',
    'option': 'A) 2 B) 2.5 C) 3 D) Error',
    'answer': 'B'
    },
    {
    'prompt': 'Who was the first President of the United States?',
    'option': 'A) George Washington B) Thomas Jefferson C) Abraham Lincoln D) Franklin',
    'answer': 'A'
    },
    {
    'prompt': 'What is the largest planet in our solar system?',
    'option': 'A) Earth B) Saturn C) Jupiter D) Uranus',
    'answer': 'C'
    },
    {
    'prompt': 'If x + 5 = 11, what is the value of x?',
    'option': 'A) 5 B) 6 C) 7 D) 8',
    'answer': 'B'
    }
]

def play_quiz(questions):
    score = 0
    for ques in questions:
        print(ques["prompt"])
        print(ques["option"])
        answer = input("Enter A, B, C, or D: ")
        if answer == ques["answer"]:
            print("Correct Answer")
            score += 1
        else:
            print("The Correct Answer is", ques["answer"])
    print(f"The total score is {score}")

play_quiz(questions)
