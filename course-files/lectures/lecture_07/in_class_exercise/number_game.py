# Instructions:
# https://docs.google.com/document/d/1mqHKMTGpX6XN7r2_cQmavrnJbpS_M4owyc5FWshtwQo/edit?usp=sharing
import random
secret_number = random.randint(1, 100)
user_guess = None
number_of_guesses = 0

def display_secret_number(secret_number):
    message = 'The secret number is (for debugging purposes): ' + str(secret_number)
    print('-' * len(message))
    print(message)
    print('-' * len(message))

display_secret_number(secret_number)
while True:
    user_guess = input('Guess a number between 1 and 100: ')
    print('Your guess is:', user_guess)
    # Your code below:
    # If the number is too low, it tells the user the number is too low and to guess again
    # If the number is too high, it tells the user the number is too high and that they should guess again
    # If they guess the number correctly:
    #  1) Tell them that they guess correctly and the number of guesses it took to guess correctly
    #  2) Exit the program (i.e. break out of the loop)
    # If they type the letter 'Q', exit the program (i.e. break out of the loop)

