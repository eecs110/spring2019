import psonic
print('Reminder: Make sure that Sonic Pi is open and running on your computer!')

########################
# FUNCTION DEFINITIONS #
########################

def play_happy_birthday(notes: list):
    '''
    Plays happy birthday by interoperating with Sonic Pi and the psonic module
    Args: 
        notes(list): a list of MIDI notes (ints)
    Returns: 
        does not return anything (None)
    '''
    psonic.use_synth(psonic.PIANO)
    psonic.play(notes[0])
    psonic.sleep(0.25)
    psonic.play(notes[1])
    psonic.sleep(0.15)
    psonic.play(notes[2])
    psonic.sleep(0.5)
    psonic.play(notes[3])
    psonic.sleep(0.5)
    psonic.play(notes[4])
    psonic.sleep(0.5)
    psonic.play(notes[5])
    # Exercise 1: Finish this song


def drum_4_beats(tempo: float, sound_sample: psonic.Sample=psonic.DRUM_HEAVY_KICK):
    '''
    Plays 4 drum hits at a given tempo (as specified by the tempo argument)
    using the sound sample (as specified by the sound_sample argument). Each
    drum hit will change in pitch.
    Args: 
        tempo(float): a float that specifies how long to wait in between beats
        sound_sample(psonic.Sample, optional): the sound sample to be used as your beat 
            (see spreadsheet for a list of available samples)
    Returns: 
        Nothing. This function's job is to output something to your speaker. It
        does not return a value.
    '''
    # Exercise 2: update the hard coded drum sample and sleep time so that it honors the 
    # tempo and sound_sample that is specified by the arguments. Currently, everything is
    # hard coded.
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)  # default rate
    psonic.sleep(0.125)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=5)
    psonic.sleep(0.125)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=10)
    psonic.sleep(0.125)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=15)
    psonic.sleep(0.125)

def add_octave(note: int, num_octaves: int=1):
    '''
    Adds num_octaves to the note. So, if the note=48, and num_octaves=1, then 
    the function will return 48 + 12 (b/c in MIDI, getting to the next octave
    is achieved by adding 12 to the note).
    Args: 
        note(int): a MIDI note, represented as an int (required)
        num_octaves(int, optional): an int representing the number of octaves you want 
            to add or subtract from the note. Defaults to 1.
    Returns: 
        Returns an int that represents a MIDI note in the designated octave
    '''
    # Exercise 3: implement this simple function
    pass

def play_c_scale(octave: int, tempo: float=0.5):
    '''
    Plays a C scale at the designated octave and tempo.
    Args: 
        octave(int): an int corresponding to the octave of the scale.
        tempo(float, optional): a float that specifies how long to wait in between notes.

    Returns: 
        Nothing. This function's job is to output something to your speaker. It
        does not return a value.
    '''
    # Exercise 4: 
    # 1) make changes to the play_c_scale function body so that it honors the 
    # octave and tempo that is specified by the arguments. Currently, everything is
    # hard coded.
    # 2) use the add_octave function that you made to shift each note in the scale 
    # by the designated octave.

    psonic.use_synth(psonic.PIANO)
    psonic.play(48)  # these are MIDI note numbers
    psonic.sleep(0.5)
    psonic.play(50)
    psonic.sleep(0.5)
    psonic.play(52)
    psonic.sleep(0.5)
    psonic.play(53)
    psonic.sleep(0.5)
    psonic.play(55)
    psonic.sleep(0.5)
    psonic.play(57)
    psonic.sleep(0.5)
    psonic.play(59)
    psonic.sleep(0.5)
    psonic.play(60)
    psonic.sleep(0.5)
    psonic.play(59)
    psonic.sleep(0.5)
    psonic.play(57)
    psonic.sleep(0.5)
    psonic.play(55)
    psonic.sleep(0.5)
    psonic.play(53)
    psonic.sleep(0.5)
    psonic.play(52)
    psonic.sleep(0.5)
    psonic.play(50)
    psonic.sleep(0.5)
    psonic.play(48)

    # play arpeggio (w/o sleep functions, notes play simultaneously):
    psonic.sleep(1)
    psonic.play(48)
    psonic.play(52)
    psonic.play(55)
    psonic.play(60)
    psonic.sleep(1)




##################
# FUNCTION CALLS #
##################

print('Exercise 1...')
play_happy_birthday([
    48, 48, 50, 48, 53, 52, 48, 48, 50, 48, 55, 53,
    48, 48, 60, 57, 53, 52, 50, 58, 58, 57, 53, 55, 53
])

print('Exercise 2...')
drum_4_beats(1)
drum_4_beats(0.5, sound_sample=psonic.DRUM_SPLASH_HARD)
drum_4_beats(0.25, sound_sample=psonic.ELEC_SNARE)

print('Exercise 3...')
print('If I add 1 octave to 48, I get:', add_octave(48))
print('If I add 2 octaves to 48, I get:', add_octave(48, num_octaves=2))
# assert add_octave(48) == 60, 'add_octave did not work as expected'
# assert add_octave(48, num_octaves=2) == 72, 'add_octave did not work as expected'

print('Exercise 4...')
play_c_scale(2)
play_c_scale(3, tempo=0.5)
play_c_scale(4, tempo=0.15)