import threader
import psonic
import my_music

controller = threader.SonicPiController(tempo=60, riff=my_music.play_base_beat)
loop_1 = threader.SonicPiLoop(controller, my_music.riff_1)
loop_2 = threader.SonicPiLoop(controller, my_music.riff_2)
loop_3 = threader.SonicPiLoop(controller, my_music.riff_3)

def start_music_loop():
    controller.start(sample=psonic.DRUM_BASS_SOFT)
    loop_1.start()
    loop_2.start()
    loop_3.start()


def kill_threads_and_close():
    print('Stopping loops...')
    loop_1.stop()
    loop_2.stop()
    loop_3.stop()
    controller.stop()


def show_menu():
    input('\nPress any key to continue...')
    header_length = 28
    print()
    print('*' * header_length)
    print('Select option from the menu')
    print('*' * header_length)
    print('1 - toggle riff 1 (' + ('on' if loop_1.is_running() else 'off') + ')')
    print('2 - toggle riff 2 (' + ('on' if loop_2.is_running() else 'off') + ')')
    print('3 - toggle riff 3 (' + ('on' if loop_3.is_running() else 'off') + ')')
    print('4 - slow down')
    print('5 - speed up')
    print('q - quit')
    print('*' * header_length)
    print()


####################
# GLOBAL VARIABLES #
####################

start_music_loop()


###################
# USER INPUT LOOP #
###################
command = ''
while command.upper() != 'Q':
    show_menu()
    command = input("What would you like to do? ")
    print('\nYou selected:')
    if command == '1':
        # replace print statement with code that toggles riff_1 on / off
        print('\n1 - TODO: toggle riff_1 on / off...')
    elif command == '2':
        # replace print statement with code that toggles riff_2 on / off
        print('\n2 - TODO: toggle riff_3 on / off...')
    elif command == '3':
        # replace print statement with code that toggles riff_3 on / off
        print('\n3 - TODO: toggle riff_3 on / off...')
    elif command == '4':
        # replace print statement with code that slows down the music
        print('\n4 - TODO: slow down the music...')
    elif command == '5':
        # replace print statement with code that speeds up the music
        print('\n5 - TODO: speed up the music...')
    elif command.upper() == 'Q':
        kill_threads_and_close()
        break