import psonic
import random

e = psonic.chord(psonic.E2, psonic.MINOR) + \
    psonic.chord(psonic.E3, psonic.MINOR) + \
    psonic.chord(psonic.E4, psonic.MINOR)
print(e)

# Challenge: Write a while loop that randomly plays a note from the 
# e minor cord, for either 0.25, or 0.5 length of time
# after it plays 30 notes it should stop
counter = 0
while counter < 30:
    psonic.use_synth(psonic.PROPHET)
    psonic.play(random.choice(e), release=0.6)
    psonic.sleep(random.choice([0.25, 0.5]))
    counter += 1