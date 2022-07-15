#!/usr/bin/env python
# coding: utf-8

# Have the computer generate a random #
# Have the user enter a number
# if the number is correct end the program and congratulate the user
# if the number is not correct repeat asking the user for the number
import random


def ask_user(number: int):
    user_guess = input("Guess the number: ")
    int_user_guess = int(user_guess)

    if number == int_user_guess:
        return True
    else:
        if int_user_guess > number:
            print("You are too high!! Guess a lower number")
        if int_user_guess < number:
            if (int_user_guess / number * 100) >= 90:
                print("You are super hot.\n")
            if (int_user_guess / number * 100) >= 75 and (int_user_guess / number * 100) < 90:
                print("You are getting hot.\n")
            if (int_user_guess / number) * 100 >= 50 and (int_user_guess / number) * 100 < 75:
                print("You are warm.\n")
            if (int_user_guess / number) * 100 < 50 and (int_user_guess / number) * 100 >= 15:
                print("You are cold.\n")
            if (int_user_guess / number) * 100 < 15:
                print("You are freezing.\n")
        return False


def guess_game(num):
    try:
        is_correct = False
        while not is_correct:
            is_correct = ask_user(num)
        print(f"Congratulations you guessed the number.\n")
    except Exception as e:
        print(f"Error {e}")



# Generate a random number between 1 and 1000
random_number = random.randint(1, 1000000)

# Start the game
guess_game(random_number)

