def move_avatar(direction, units):
    if direction == 'up':
        print('subtract', units, 'from y-position')
    elif direction == 'down':
        print('add', units, 'to y-position')
    elif direction == 'left':
        print('subtract', units, 'to x-position')
    elif direction == 'right':
        print('add', units, 'to x-position')

move_avatar('up', 10)
move_avatar('down', 15)
move_avatar('left', 2)
move_avatar('right', 3)