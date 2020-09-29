def key_color(fore_color = 'black', back_color = 'brown',
              link_color = 'blue', visited_color = 'yellow'):
    return '{}, {}, {}, {}'.format(fore_color, back_color, link_color, visited_color)

def key_color_args_kwargs(*args, **kwargs):
    color_values = []
    for color in args:
        color_values.append(color)
    for color_item in kwargs:
        color_values.append(kwargs.get(color_item))

    return '{}, {}, {}, {}'.format(*color_values)