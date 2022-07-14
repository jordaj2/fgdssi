# Have the comoputer generate a random #
# Have the user enter a number
# if the number is correct end the program and congratulate the user
# if the number is not correct repeat asking the user for the number
import random


def ask_user(number:int):
    user_guess = ""
    try:
        user_guess = input("Guess the number")
        user_guess = int(user_guess)
    except Exception:
        print(f"{user_guess} is not a number.  Try Again")
        return False
    if number == user_guess:
        return True
    else:
        if user_guess > number:
            print("You are way to high!! Guess a lower number")
        if user_guess < number:
            if (user_guess/number * 100) > 75:
                print("You are getting hot")
            if (user_guess/number) * 100 > 50 and (user_guess/number) * 100 < 75:
                print("You are warm")
            if (user_guess/number) * 100 < 50 and (user_guess/number) * 100 > 15:
                print("You are cold")
            if (user_guess/number) * 100 < 15:
                print("You are freezing")
        return False



def guess_game(num):
    try:
        is_correct = False
        while not is_correct:
            is_correct = ask_user(num)
        print(f"Congratulations you guessed the number")
    except Exception as e:
        print(f"Error {e}")


# Generate a random number between 1 and 1000
random_number = random.randint(1, 1000)


# Start the game
guess_game(random_number)

