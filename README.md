# Guess Me Game 🎯

A simple number guessing game built in Python where the computer picks a random number and gives you hot/cold hints as you try to guess it.

## How It Works

The computer randomly selects a number between 1 and 100. You then try to guess the number, and after each guess you'll receive a hint based on how close you are:

- **COLD** – your guess is more than 10 away from the number
- **WARM** – your guess is within 10 of the number
- **COLDER** – your latest guess is farther away than your previous guess
- **WARMER** – your latest guess is closer than your previous guess
- **CONGRATULATIONS** – you got it!

Guesses outside the range of 1–100 are rejected as out of bounds.

## Example Gameplay

```
WELCOME TO GUESS ME GAME!
I'm thinking of a number between 1 and 100.
...
What is your guess? 50
COLD!
What is your guess? 75
WARMER!
What is your guess? 82
COLDER!
What is your guess? 78
CONGRATULATIONS! YOU GUESSED IT IN ONLY 4 GUESSES!!
```

## File Structure

```
hello world.py   # Main game script
README.md          # This file
```

