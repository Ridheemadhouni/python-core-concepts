# Number Guessing Game

A simple Number Guessing Game made using Python.

The computer randomly selects a number between 1 and 100, and the player has to guess the number. After every guess, the game gives a hint telling whether the guess is too high or too low.

## Features

* Random number generation
* User input
* High and low hints
* Counts the number of attempts
* Handles invalid input
* Simple beginner-friendly Python project

## Technologies Used

* Python
* Random module

## Project Structure

```text
Number_Guessing_Game/
│
├── main.py
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd Number-Guessing-Game
```

### 3. Run the Python File

```bash
python number_guessing_game.py
```

## How to Play

1. The computer chooses a random number from 1 to 100.
2. Enter your guess.
3. The game provides a hint:

   * Too low: Guess a higher number.
   * Too high: Guess a lower number.
   * Correct: You win.
4. The game displays the number of attempts taken.

## Example

```text
Welcome to the Number Guessing Game!
I have selected a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Congratulations! You guessed the correct number.
You guessed it in 3 attempts.
```

## Concepts Used

This project helps practice:

* Variables
* input()
* Type conversion
* if, elif, and else
* while loop
* try-except
* Random number generation
* f-strings

## Author

Ridhima Dhoni
