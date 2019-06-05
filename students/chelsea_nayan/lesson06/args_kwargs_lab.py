# Lesson06: args and kwargs lab

def color(fore_color="red", back_color="orange", link_color="yellow", visited_color="green"):
    return(print(fore_color, back_color, link_color, visited_color))

color()
color('red', 'blue', 'yellow', 'chartreuse')
color(link_color='red', back_color='blue')
color('purple', link_color='red', back_color='blue')

regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
color(*regular, **links)
