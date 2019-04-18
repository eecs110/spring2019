def change_song_speed(direction, units):
    if direction == 'up':
        # make the song faster by decreasing the wait time between notes:
        print('make the sleep interval shorter by', units, 'milliseconds')
    elif direction == 'down':
        # make the song slower by increasing the wait time between notes:
        print('make the sleep interval longer by', units, 'milliseconds')
    else:
        print(direction, 'is not a valid direction. Please use "up" or "down"')

change_song_speed('up', 10)
change_song_speed('down', 15)