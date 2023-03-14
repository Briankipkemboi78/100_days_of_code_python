from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it. The answer is {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)
    turns = set_difficulty()

    print(f"You have {turns} attempts remaining to guess the number")

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: \n"))
        check_answer(guess, answer)

game()
