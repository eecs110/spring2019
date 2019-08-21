import psonic
import random

def play_base_beat(tempo:float=60, sample=psonic.DRUM_BASS_SOFT):
    speed = 60 / tempo
    for i in range(2):
        if sample:
            psonic.sample(sample)
        psonic.sleep(speed)
    

def riff_1(tempo:float=60):
    speed = tempo / 60 * 2
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(0.20 * speed)

def riff_2(tempo:float=60):
    speed = 60 / tempo
    for i in range(3):
        psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)
        psonic.sleep(speed * 0.5)
    psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)

def riff_3(tempo:float=60):
    speed = 60 / tempo
    psonic.use_synth(psonic.PROPHET)
    sc = psonic.scale(psonic.E2, psonic.MINOR)
    s = random.choice([
        0.125 * speed,
        0.25 * speed,
        0.5 * speed
    ])
    for i in range(8):
        r = random.choice([0.125, 0.25, 1, 2])
        n = random.choice(sc)
        co = random.randint(30,100)
        psonic.play(n, release = r, cutoff = co)
        psonic.sleep(s)