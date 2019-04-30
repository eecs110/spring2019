import random
import psonic

# Challenge: write a loop that plays 128 beats, using the 
# psonic.DRUM_BASS_HARD sample, that are each at a different
# pitch (from 1 to 10). Note that pitch is controlled by the "rate" keyword argument.
for n in range(128):
    print(n, 'of 128')
    r = random.randrange(1,10)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=r)
    psonic.sleep(0.125)