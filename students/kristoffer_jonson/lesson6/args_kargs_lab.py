def print_colors(fore_color ='white', back_color = 'white', link_color = 'white', visited_color = 'white'):
    return (fore_color, back_color,link_color,visited_color)

def print_colors_args(*args,**kwargs):
    print('positional arguments are ',args)
    print('keyword arguments are ',kwargs)
    fore_color = args[0]
    back_color = args[1]
    link_color = kwargs['link_color']
    visited_color = kwargs['visited_color']
    return (fore_color, back_color,link_color,visited_color)