import psonic

def make_song():
    # do something interesting here with sound:
    psonic.use_synth(psonic.PIANO)
    psonic.play(76)
    psonic.sleep(0.25)
    psonic.play(76)
    psonic.sleep(0.5)
    psonic.play(76)
    psonic.sleep(0.5)
    psonic.play(72)
    psonic.sleep(0.25)
    psonic.play(76)
    psonic.sleep(0.5)
    psonic.play(79)
    psonic.sample(psonic.DRUM_CYMBAL_SOFT)
    psonic.sleep(1)
    psonic.play(67)
    psonic.sample(psonic.DRUM_BASS_HARD)
    psonic.sleep(1)

    # ...