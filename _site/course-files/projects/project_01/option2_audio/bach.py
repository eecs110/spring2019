import psonic
import threader

psonic.use_synth(psonic.PLUCK)

def high_part(tempo=60):
    psonic.play_pattern_timed(74, 0.5)
    psonic.play_pattern_timed([67, 69, 71, 72], 0.25)
    psonic.play_pattern_timed([74, 67, 67], 0.5)
    psonic.play_pattern_timed(76, 0.5)
    psonic.play_pattern_timed([72, 74, 76, 78], 0.25)
    psonic.play_pattern_timed([79, 67, 67], 0.5)
    psonic.play_pattern_timed(72, 0.5)
    psonic.play_pattern_timed([74, 72, 71, 69],0.25)
    psonic.play_pattern_timed(71, 0.5)
    psonic.play_pattern_timed([72, 71, 69, 67], 0.25)
    psonic.play_pattern_timed(66, 0.5)
    psonic.play_pattern_timed([67, 69, 71, 67], 0.25)
    psonic.play_pattern_timed([71, 69], 0.5)


def low_part(tempo=60):
    psonic.play([55,59])
    psonic.sleep(1)
    psonic.play_pattern_timed(57, 0.5)
    psonic.play_pattern_timed([59, 60, 59, 57, 55], 1.5)
    psonic.play_pattern_timed([62, 59, 55, 62], 0.5)
    psonic.play_pattern_timed([50, 60, 59], 0.25)
    psonic.play(57)



high_part()
low_part()



# Uncomment the section below 
# (and comment the function calls above)
# to play the two parts together:

# def controller_riff(tempo):
#     psonic.sample(psonic.DRUM_BASS_SOFT, amp=0.5, rate=7)
#     psonic.sleep(1.5)


# # Play 
# controller = threader.SonicPiController(tempo=60, riff=controller_riff)
# controller.start()
# low_loop_thread = threader.SonicPiLoop(controller, low_part)
# high_loop_thread = threader.SonicPiLoop(controller, high_part)
# low_loop_thread.start()
# high_loop_thread.start()