import random

def number_guessing():
    print("Welcome to number guessing game!")
    print("Try to guess number between 1 and 100.")

    random_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_number = int(input("Enter your number: "))
            attempts += 1

            if user_number < random_number:
                print("Too low!")
            elif user_number > random_number:
                print("Too high!")
            else:
                guessed = True
                print(f"Congratulations! you've guess the number in {attempts} attepmts")
        except ValueError:
            print("Invalid number! Please enter corrent number")
number_guessing()    

            




