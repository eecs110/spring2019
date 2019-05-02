import psonic

midi_notes_low_part = [
    ([55, 59], None),
    (None, 1),
    (57, 0.5),
    ([59, 60, 59, 57, 55], 1.5),
    ([62, 59, 55, 62], 0.5),
    ([50, 60, 59], 0.25),
    (57, None)
]

midi_notes_high_part = [
    (74, 0.5),
    ([67, 69, 71, 72], 0.25),
    ([74, 67, 67], 0.5),
    (76, 0.5),
    ([72, 74, 76, 78], 0.25),
    ([79, 67, 67], 0.5),
    (72, 0.5),
    ([74, 72, 71, 69], 0.25),
    (71, 0.5),
    ([72, 71, 69, 67], 0.25),
    (66, 0.5),
    ([67, 69, 71, 67], 0.25),
    ([71, 69], 0.5)
]


# When you're done, here is how you should call your function:
# play_song(60, midi_notes_low_part)
# play_song(60, midi_notes_high_part)