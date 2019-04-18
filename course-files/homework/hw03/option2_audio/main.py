import helpers
import psonic
import music

music.make_song()
music.make_song(synth=psonic.PLUCK)
music.make_song(tempo=2, synth=psonic.PROPHET, sound_sample=psonic.DRUM_SPLASH_SOFT)
music.make_song(tempo=0.5, synth=psonic.SUPERSAW, sound_sample=psonic.DRUM_COWBELL)
