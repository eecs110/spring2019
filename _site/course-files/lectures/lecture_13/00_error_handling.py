# This loop keeps going until the user has entered a valid age:
while True:
    age = input('enter your age: ')
    year = input('enter a year in the future: ')
    print('Your age in 2050:', int(age) + int(year) - 2019)

    up_next = input('Do you want to try again (Y/n)?' )
    if up_next.upper() == 'N':
        # Exit the loop...
        print('exiting...\n')
        break