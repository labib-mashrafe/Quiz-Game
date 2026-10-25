# Quiz Game CLI
import random
import json

QUESTIONS_FILE="questions.json"

def load_questions():
    try:
        with open(QUESTIONS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    
def run_quiz():
    questions = load_questions()
    if not questions:
        print("Could not load questions. Make sure questions.json exists and is valid.")
        return
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
