# args_kwarg_lab.py #
"""
Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color
Have it return the colors (use strings for the colors, e.g. “blue” etc.)
Call it with a couple different parameters set. That is, write tests that
verify that all of the following work as advertised:
1. Using just positional arguments:
func('red', 'blue', 'yellow', 'chartreuse')
2. Using just keyword arguments:
func(link_color='red', back_color='blue')
3. Using a combination of positional and keyword
``func('purple', link_color='red', back_color='blue')
4. Using *some_tuple and/or **some_dict
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func(*regular, **links)
"""
# def func(spam, eggs=1, *args, foo, bar=2, **kwargs):
#         print(spam, eggs, args, foo, bar, kwargs)

def return_colors(fore_color='black', back_color='black', link_color='black',
                  visited_color='black'):
    #color_list = [fore_color, back_color, link_color, visited_color]
    #return color_list
    return [fore_color, back_color, link_color, visited_color]

def return_colors_args_kwargs(fore_color='black', back_color='black',
                              *args, link_color='black', visited_color='black',
                              **kwargs):
    #color_list = [fore_color, back_color, args, link_color, visited_color,
    #              kwargs]
    print(f"-- args:{args}, kwargs:{kwargs} --")
    return [fore_color, back_color, args, link_color, visited_color, kwargs]
