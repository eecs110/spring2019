import psonic

# These are just some simple riffs (placeholders)
# replace these with your own!

def controller_riff(tempo):
    speed = 60 / tempo
    # very low volume controller beat (just for debugging):
    psonic.sample(psonic.DRUM_BASS_SOFT, amp=0.2, rate=7)
    psonic.sleep(speed)

def riff_1a(tempo=60):
    speed = 60 / tempo
    for i in range(5):
        psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)
        psonic.sleep(speed * 0.5)
    psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)

def riff_1b(tempo=60):
    speed = 60 / tempo
    for i in range(7):
        psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)
        psonic.sleep(speed * .125)
    psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)

def riff_2(tempo=60):
    speed = 60 / tempo
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT)

def riff_3(tempo=60):
    speed = 60 / tempo
    psonic.sample(psonic.AMBI_LUNAR_LAND)
    #psonic.sample(psonic.AMBI_DRONE)
    psonic.sleep(3.99 * speed) # make the last sleep a little shorter
