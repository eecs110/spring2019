def print_menu():
    print('''
1 - Search for a restaurant
2 - Browse comments
3 - Set / view preferences
4 - Quit
    ''')

while True:
    print_menu()
    choice = input('What would you like to do? ')
    if choice == '1':
        print('search for a restaurant...')
    if choice == '2':
        print('browse comments...')
    if choice == '3':
        print('set / view preferences...')
    if choice == '4':
        print('Quitting...')
        break
    input('\nPress any key to continue...')
