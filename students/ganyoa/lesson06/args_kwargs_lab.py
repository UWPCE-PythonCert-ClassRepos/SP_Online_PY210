def colors(fore_color="red", back_color="blue", link_color="yellow", visited_color="chartreuse"):
    return[fore_color, back_color, link_color, visited_color]

regular = ('black', 'green')
links = {'link_color': 'pink', 'visited_color': 'teal'}




def colors_args(*args, **kwargs):
     print('args: ', args)
     print('kwargs: ', kwargs)
     return list(args + tuple((kwargs.values())))

#colors_args('black', 'green', link_color = 'pink', visited_color = 'teal')
