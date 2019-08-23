"""
Programming In Python - Lesson 6 Exercise 2: Args & Kwargs Lab
Code Poet: Anthony McKeever
Start Date: 08/22/2019
End Date: 08/22/2019
"""

def colorful_args(fore_color="magenta", back_color="cyan", link_color="yellow", visited_color="black"):
    return [fore_color, back_color, link_color, visited_color]


def colorful_args_kwargs(*args, **kwargs):
    print("Positional Args:", args)
    print("Keyword Args:", kwargs)

    colorful_list = ["magenta", "cyan", "yellow", "black"]

    fore_color = kwargs.get("fore_color") if kwargs.get("fore_color") is not None else args[0] if len(args) >= 1 else colorful_list[0]
    back_color = kwargs.get("back_color") if kwargs.get("back_color") is not None else args[1] if len(args) >= 2 else colorful_list[1]
    link_color = kwargs.get("link_color") if kwargs.get("link_color") is not None else args[2] if len(args) >= 3 else colorful_list[2]
    visited_color = kwargs.get("visited_color") if kwargs.get("visited_color") is not None else args[3] if len(args) >= 4 else colorful_list[3]
    
    return [fore_color, back_color, link_color, visited_color]
