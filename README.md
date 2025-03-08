# Day-4-Rock-Paper-Scissors
Rock Paper Scissors Game - Difficulty: Easy

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/08

## License:
MIT License

## Dependencies:
None (built-in functions only)

## Description:
rockPaperScissors.py is a simple Python script that allows you to play the classic game of Rock, Paper, Scissors against the computer. The game works by comparing the player's choice to the computer's randomly generated choice. The script prompts the player to select one of the three options: Rock, Paper, or Scissors.

The following inputs are expected from the player:

0 for Rock

1 for Paper

2 for Scissors

The script then generates a random choice for the computer, compares it with the player's choice, and determines the winner (or if there's a tie).

## Usage:
Clone this repository:
```bash
git clone https://github.com/CarlosValerioM/Day-4-Rock_Paper_Scissors.git
```
Navigate to the project directory:
```bash
cd Day-4-Rock_Paper_Scissors
```
Run the script:

```python
python rockPaperScissors.py
```
The script will prompt you to choose between Rock, Paper, or Scissors, and then display the result of the game (Win, Lose, or Tie).

## Example Output:
```python
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: 0
    _______
---'    ____)
       (_____)
       (_____)
       (____)
- --._(___)

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

It's a tie!
```
## How it works:
The player inputs their choice of Rock (0), Paper (1), or Scissors (2).

The computer generates a random number between 0 and 2 to represent its choice.

The script compares both choices:

Rock (0) beats Scissors (2)

Scissors (2) beats Paper (1)

Paper (1) beats Rock (0)

If both choices are the same, it results in a tie.

The script then displays the result: "You Win!", "You Lose!", or "It's a tie!"

## License:
This project is licensed under the MIT License.
