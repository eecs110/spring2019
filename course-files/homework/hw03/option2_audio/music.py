import psonic

def make_song(tempo=1, synth=psonic.PIANO, sound_sample=psonic.DRUM_CYMBAL_SOFT):
    # do something interesting here with sound:
    psonic.use_synth(synth)
    psonic.play(76)
    psonic.sleep(0.25 * tempo)
    psonic.play(76)
    psonic.sleep(0.5 * tempo)
    psonic.play(76)
    psonic.sleep(0.5 * tempo)
    psonic.play(72)
    psonic.sleep(0.25 * tempo)
    psonic.play(76)
    psonic.sleep(0.5 * tempo)
    psonic.play(79)
    psonic.sample(sound_sample)
    psonic.sleep(1 * tempo)
    psonic.play(67)
    psonic.sample(sound_sample)
    psonic.sleep(1 * tempo)

    # ...