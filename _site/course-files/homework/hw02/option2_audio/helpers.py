# psonic documentation: # https://github.com/gkvoelkl/python-sonic
# MIDI Reference: http://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
# play function reference: https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=860514818
# TODO: Ensure that your Sonic Pi is running before you run this Python file


import random
import psonic
play = psonic.play      # shortcut (aliasing for less typing)
sleep = psonic.sleep    # shortcut (aliasing for less typing)
sample = psonic.sample

SUPER_MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71,
    79, 78, 77, 75, 76, 68, 69, 72, 69, 72, 74, 79,
    78, 77, 75, 76, 84, 79, 78, 77, 75, 76, 68, 69,
    72, 69, 72, 74, 75, 74, 72, 72, 74, 76, 72, 69,
    67, 72, 74, 76, 72, 74, 76, 72, 69, 67, 76, 72,
    76, 79, 67, 76, 72, 67, 68, 69, 77, 69, 71, 81,
    79, 77, 76, 72, 69, 67, 76, 72, 67, 68, 69, 77,
    69, 71, 77, 76, 74, 72
]
SUPER_MARIO_NOTES_FIRST_24 = SUPER_MARIO_NOTES[0:24]


def demo_play_sustain():
    # controls how long the note lasts
    psonic.use_synth(psonic.SUBPULSE)  # select a synthesizer:
    play(48)  # default
    sleep(1)
    play(50, sustain=1)  # a little longer
    sleep(1)
    play(52, sustain=2)  # a little longer
    sleep(1)
    play(53, sustain=4.5)  # even longer
    sleep(1)


def demo_play_volume_adjust():
    # controls how loud the note lasts
    psonic.use_synth(psonic.SUBPULSE)
    play(48)  # default
    sleep(1)
    play(50, sustain_level=0.2)  # soft
    sleep(1)
    play(52, sustain_level=0.4)  # a little louder
    sleep(1)
    play(53, sustain_level=0.6)  # even louder
    sleep(1)
    play(55, sustain_level=1.6)  # even louder
    sleep(1)


def demo_play_fadein():
    # controls the fade-in time
    psonic.use_synth(psonic.SUBPULSE)
    play(48)  # default
    sleep(1)
    play(50, attack=0.5)  # fade in
    sleep(1)
    play(52, attack=1)  # longer fade in
    sleep(1)
    play(53, attack=2)  # even longer fade in
    sleep(1)


def demo_play_fadeout():
    # controls the time it takes to fade-out time
    psonic.use_synth(psonic.SUBPULSE)
    play(48)  # default
    sleep(1)
    play(50, release=0.1)  # fade out
    sleep(1)
    play(52, release=0.2)  # longer fade in
    sleep(1)
    play(53, release=0.6)  # even longer fade in
    sleep(1)


def demo_play_combo():
    # demonstration of the optional parameters available using
    # the play function. To read about these, take a look at the
    # spreadsheet of documentation that I made for you:
    # https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=860514818
    psonic.use_synth(psonic.SUBPULSE)
    play(48, amp=0.2, sustain=2, attack=1, decay=1)


def play_super_mario():
    # play the first 24 notes of Super Mario Brothers theme music
    # audio demo: https://vimeo.com/85685770
    psonic.use_synth(psonic.PIANO)
    play(SUPER_MARIO_NOTES_FIRST_24[0])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[1])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[2])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[3])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[4])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[5])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[6])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[7])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[8])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[9])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[10])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[11])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[12])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[13])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[14])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[15])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[16])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[17])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[18])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[19])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[20])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[21])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[22])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[23])
    sleep(0.1)


##########################
## Working with Samples ##
##########################
# For a list of all of the samples:
# https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=195217270

def drum_4_beats():
    # Note: rate controls how far the sample is stretched
    sample(psonic.DRUM_BASS_HARD, rate=1)  # default rate
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=5)
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=10)
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=15)
    sleep(0.125)


def drum_3_random_beats():
    sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
    sleep(0.125)


def drum_continuous_random_beats():
    import random
    while True:
        sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
        sleep(0.125)
        # Note: type Control C to cancel.


def drum_continuous_low_beats():
    while True:
        sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 5))
        sleep(0.125)
        # Note: type Control C to cancel.


def drum_continuous_high_beats():
    while True:
        sample(psonic.DRUM_HEAVY_KICK, rate=random.randrange(30, 50))
        sleep(0.125)
        # Note: type Control C to cancel.


def vinyl_scratch():
    sample(psonic.VINYL_HISS)
    sleep(2)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)


def custom_sound():
    # play any wav file that you choose (just save it in the same directory)
    # you can download them from the internet (e.g. https://freewavesamples.com/)
    # or make your own:
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sound_file = os.path.join(dir_path,'sounds/harley_davidson.wav')
    start = 0.2  # float between 0 and 1
    finish = 0.3  # float between 0 and 1
    file_path = os.path.abspath(sound_file)
    command = 'sample "{0}", start: {1}, finish: {2}'.format(
        file_path, start, finish)

    psonic.run(command)


###################
## MIDI EXAMPLES ##
###################
print('Reminder: Make sure that Sonic Pi is open and running on your computer!')
demo_play_sustain()
demo_play_fadein()
demo_play_fadeout()
play_super_mario()

#######################
## SAMPLES: EXAMPLES ##
#######################
drum_4_beats()
drum_3_random_beats()
vinyl_scratch()
custom_sound()
