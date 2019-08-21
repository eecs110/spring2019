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
    if user_guess.upper() == 'Q':
        break
    user_guess = int(user_guess)
    number_of_guesses += 1
    if user_guess > secret_number:
        print('Too high. Try again!')
    elif user_guess < secret_number:
        print('Too low. Try again!')
    else:
        print('You win in', number_of_guesses, 'guesses', end='!\n')
        break

print('Game over!')