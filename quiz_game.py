# Quiz Game CLI
import random

def run_quiz():
    questions = [
        {"question": "What is the capital of France?",
         "options": ["London", "Paris", "Rome", "Berlin"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?",
         "options": ["Venus", "Jupiter", "Mars", "Saturn"], "answer": "C"},
        {"question": "What is 5 + 7?",
         "options": ["12", "10", "13", "11"], "answer": "A"},
        {"question": "Who wrote Hamlet?",
         "options": ["Dickens", "Tolstoy", "Homer", "Shakespeare"], "answer": "D"},
        {"question": "What is the largest ocean?",
         "options": ["Atlantic", "Pacific", "Indian", "Arctic"], "answer": "B"}
    ]
    random.shuffle(questions)
    
    score = 0

    print("Welcome to the Quiz Game! Answer the questions below:\n")

    for idx, q in enumerate(questions, 1):
        print(f"{idx}. {q['question']}")
        for letter, option in zip("ABCD", q["options"]):
            print(f"   {letter}) {option}")

        while True:
            user_answer = input("Your answer: ").strip().upper()
            if user_answer in ("A", "B", "C", "D"):
                break
            print("Please enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_option = q["options"]["ABCD".index(q["answer"])]
            print(f"Wrong! Correct answer: {q['answer']}) {correct_option}\n")

    print(f"Quiz complete! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()
