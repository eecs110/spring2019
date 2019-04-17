def make_creature(canvas, position, width=200, primary_color='tan', secondary_color='#916f45'):
    print('make_creature(canvas, {0}, width={1}, primary_color=\'{2}\', secondary_color=\'{3}\')'.format(
        position, width, primary_color, secondary_color
    ))
    x = position[0]
    y = position[1]
    eye_width = width * 0.15
    eye_height = width * 0.15
    ear_width = width / 2
    anchor_x = x - width / 2
    anchor_y = y - width / 2
    left_eye_offset_x = x - eye_width + width * 0.2
    right_eye_offset_x = x - width * 0.2
    left_eye_offset_y = y - width * 0.2
    right_eye_offset_y = left_eye_offset_y


    face = canvas.create_oval(
        anchor_x,  # left
        anchor_y,  # top
        anchor_x + width,  # right
        anchor_y + width,  # bottom
        fill=primary_color,
        width=2,
        tag='creature'
    )

    left_ear = canvas.create_oval(
        x - width / 2 - ear_width / 3,  # left
        y - width / 2 - ear_width / 3,
        x - width / 2 + ear_width / 3 * 2,  # right
        y - width / 2 + ear_width / 3 * 2,  # bottom
        fill=secondary_color,
        width=2,
        tag='creature'
    )

    right_ear = canvas.create_oval(
        x + width / 2 + ear_width / 3,  # left
        y - width / 2 - ear_width / 3,
        x + width / 2 - ear_width / 3 * 2,  # right
        y - width / 2 + ear_width / 3 * 2,  # bottom
        fill=secondary_color,
        width=2,
        tag='creature'
    )

    left_eye = canvas.create_oval(
        left_eye_offset_x,  # left
        left_eye_offset_y,  # top
        left_eye_offset_x + eye_width,  # right
        left_eye_offset_y + eye_height,  # bottom
        fill='black',
        width=2,
        tag='creature'
    )

    right_eye = canvas.create_oval(
        right_eye_offset_x,  # left
        right_eye_offset_y,  # top
        right_eye_offset_x + eye_width,  # right
        right_eye_offset_y + eye_height,  # bottom
        fill='black',
        width=2,
        tag='creature'
    )

    canvas.create_polygon(
        x - width * 0.15,
        y,
        x + width * 0.15,
        y,
        x,
        y + width * 0.2,
        width=2,
        fill='black',
        smooth=True,
        tag='creature'
    )

    nose_y = y + width * 0.15
    canvas.create_line(
        x,
        nose_y,
        x,
        nose_y + width * 0.15,
        x + width * 0.2,
        nose_y + width * 0.15, width=2, smooth=True,
        tag='creature'
    )

    canvas.create_line(
        x,
        nose_y,
        x,
        nose_y + width * 0.15,
        x - width * 0.2,
        nose_y + width * 0.15, width=2, smooth=True,
        tag='creature'
    )


colors = [
    '#bfdc65',
    '#afc272',
    '#aebb83',
    '#abb880',
    '#89ba63',
    '#94ba77',
    '#94ae83',
    '#92ac82',
    '#227876',
    '#48878a',
    '#648d8e',
    '#608888',
    '#1b324d',
    '#3f5364',
    '#3b4e5f',
    '#5e6976'
]