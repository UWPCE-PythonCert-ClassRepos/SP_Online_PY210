# Arg Kwarg Code for Test Driven Development Practice #

"""Write a function that has four optional parameters (with defaults):
    -fore_color
    -back_color
    -link_color
    -visited_colo
        -Have it return the colors (use strings for the colors, e.g. “blue”, “red”, etc.)
-Call it with a couple different parameters set. That is, write tests that verify that all of the following work as advertised:

    -Using just positional arguments:
        func('red', 'blue', 'yellow', 'chartreuse')
    -Using just keyword arguments:
        func(link_color='red', back_color='blue')
        using a combination of positional and keyword
        ``func('purple', link_color='red', back_color='blue')
    -using *some_tuple and/or **some_dict
        regular = ('red', 'blue')
        links = {'link_color': 'chartreuse'}
        func(*regular, **links)"""


def color_scheme(fore_color='green', back_color='blue', link_color='gray', visited_color='orange'):
    
    color_list = [fore_color, back_color, link_color, visited_color]
    return color_list

"""Write a new function with arg and kwarg as parameters.
-Have it return the colors (use strings for the colors again)
-Call it with the same various combinations of arguments used above.
-Also have it print args and kwargs directly, so you can be sure you understand what’s going on.
-Note that in general, you can’t know what will get passed into **kwargs 
    So maybe adapt your function to be able to do something reasonable with any keywords."""

def complex_color_scheme(*args, **kwargs):
    
    print('These are the positional arguments:', args)
    print('These are the keyword arguments:', kwargs) 
    
    color_palette = []

    # Cycle through args and kwargs to get all inputs in list
    for col in args:
        color_palette.append(col)
    for color in kwargs:
        color_palette.append(kwargs.get(color))

    return color_palette


