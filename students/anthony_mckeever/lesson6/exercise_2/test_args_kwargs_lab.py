"""
Programming In Python - Lesson 6 Exercise 2: Args & Kwargs Lab Tests
Code Poet: Anthony McKeever
Start Date: 08/22/2019
End Date: 08/22/2019
"""
import args_kwargs_lab as lab

class TestColorfulArgs():
    def test_defaults(self):
        assert lab.colorful_args() == ["magenta", "cyan", "yellow", "black"]


    def test_positionals(self):
        assert lab.colorful_args("sugar almond pink", "mint green", "lemon yellow", "walnut brown") == ["sugar almond pink", "mint green", "lemon yellow", "walnut brown"]


    def test_keywords(self):
        assert lab.colorful_args(link_color="sky blue", back_color="apple pink") == ["magenta", "apple pink", "sky blue", "black"]


    def test_combo_args(self):
        assert lab.colorful_args("jade green", link_color="chrome orange", back_color="amethyst purple") == ["jade green", "amethyst purple", "chrome orange", "black"]


    def test_tuple_and_dict(self):
        colorful_tuple = ("sky blue", "floral pink")
        colorful_dictionary = {"link_color": "mallow purple", "visited_color": "navy blue"}
        assert lab.colorful_args(*colorful_tuple, **colorful_dictionary) == ["sky blue", "floral pink", "mallow purple", "navy blue"]


class TestColorfulArgsKwargs():
    def test_defaults(self):
        assert lab.colorful_args_kwargs() == ["magenta", "cyan", "yellow", "black"]


    def test_positionals(self):
        assert lab.colorful_args_kwargs("sugar almond pink", "mint green", "lemon yellow", "walnut brown") == ["sugar almond pink", "mint green", "lemon yellow", "walnut brown"]


    def test_keywords(self):
        assert lab.colorful_args_kwargs(link_color="sky blue", back_color="apple pink") == ["magenta", "apple pink", "sky blue", "black"]


    def test_combo_args(self):
        assert lab.colorful_args_kwargs("jade green", link_color="chrome orange", back_color="amethyst purple") == ["jade green", "amethyst purple", "chrome orange", "black"]


    def test_tuple_and_dict(self):
        colorful_tuple = ("sky blue", "floral pink")
        colorful_dictionary = {"link_color": "mallow purple", "visited_color": "navy blue"}
        assert lab.colorful_args_kwargs(*colorful_tuple, **colorful_dictionary) == ["sky blue", "floral pink", "mallow purple", "navy blue"]
