"""
Test code for args_kwarg_lab.py


"""
from args_kwarg_lab import return_colors, return_colors_args_kwargs

color_list_1 = ['red', 'blue', 'yellow', 'chartreuse']
color_list_2 = ['black', 'blue', 'red', 'black']
color_list_3 = ['purple', 'blue', 'red', 'black']
color_list_4 = ['red', 'blue', 'chartreuse', 'black']

def test_positional_arguments():
    returned_color_list = return_colors('red', 'blue', 'yellow', 'chartreuse')
    assert color_list_1 == returned_color_list

def test_keyword_arguments():
    returned_color_list = return_colors(link_color='red', back_color='blue')
    assert color_list_2 == returned_color_list

def test_positional_keyword_arguments():
    returned_color_list = return_colors('purple', link_color='red',
                                        back_color='blue')
    assert color_list_3 == returned_color_list

def test_tuple_dict_arguments():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    returned_color_list = return_colors(*regular, **links)
    assert color_list_4 == returned_color_list

###########################################################
color_list_5 = ['red', 'blue', ('yellow', 'chartreuse'), 'black', 'black', {}]
color_list_6 = ['black', 'blue', (), 'red', 'black', {}]
color_list_7 = ['purple', 'blue', (), 'red', 'black', {}]
color_list_8 = ['red', 'blue', (), 'chartreuse', 'black', {}]

def test_args_kwargs_positional_arguments():
    returned_color_list = return_colors_args_kwargs('red', 'blue', 'yellow',
                                                    'chartreuse')
    assert color_list_5 == returned_color_list

def test_args_kwargs_keyword_arguments():
    returned_color_list = return_colors_args_kwargs(link_color='red',
                                                    back_color='blue')
    assert color_list_6 == returned_color_list


def test_args_kwargs_positional_keyword_arguments():
    returned_color_list = return_colors_args_kwargs('purple', link_color='red',
                                                    back_color='blue')
    assert color_list_7 == returned_color_list

def test_args_kwargs_tuple_dict_arguments():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    returned_color_list = return_colors_args_kwargs(*regular, **links)
    assert color_list_8 == returned_color_list
