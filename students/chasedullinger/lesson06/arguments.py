"""
Test functions to show how different arguments work
"""

def fun_opt_kw_params(fore_color='blue', back_color='red',
                      link_color='yellow', visited_color='orange'):
    return fore_color, back_color, link_color, visited_color


def fun_star_params(*args, **kwargs):

    list_to_return = [item for item in args]

    for value in kwargs.values():
        list_to_return.append(value)
    return tuple(list_to_return)
