# Quiz Game

A multiple-choice quiz game for the terminal, written in Python. Questions are loaded from a JSON file and shuffled every round, so you can add your own questions without touching the code.

## Features

- Multiple-choice questions (A–D), with input validation that accepts only A, B, C or D
- Questions shuffled into a random order each round
- Questions stored in `questions.json`, separate from the code
- Final score with percentage and feedback: "Perfect score!" at 100%, "Good job!" at 75% or above, "Keep practising!" below 75%
- Play again without restarting the program
- Clear error message, and a clean exit, if the questions file is missing or invalid

## How to Run

Requires Python 3. Keep `questions.json` in the same folder as `quiz_game.py`.

```
python quiz_game.py
```

## Adding Questions

Add an entry to `questions.json` in this format:

```json
{
    "question": "What is the capital of Japan?",
    "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
    "answer": "C"
}
```

`answer` is the letter of the correct option.

## Example

```
1. Which planet is known as the Red Planet?
   A) Venus
   B) Jupiter
   C) Mars
   D) Saturn
Your answer: x
Please enter A, B, C, or D.
Your answer: c
Correct!

...

Quiz complete! Your final score is 4 out of 5.
That's 80%.
Good job!
Play again? (y/n): n
Thanks for playing!
```

## What I Learned

- Loading data from a JSON file and separating data from code
- Using the `random` module to shuffle a list
- Pairing lists with `zip()` and validating input
- Returning `True`/`False` from a function to control program flow

## License

MIT
