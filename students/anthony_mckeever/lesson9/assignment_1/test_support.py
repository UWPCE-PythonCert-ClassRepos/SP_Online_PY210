"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 09/15/2019
"""

import io
import sys
import os.path
import tempfile

from unittest import TestCase
from unittest import mock
from unittest.mock import patch

from support import Helpers
from support import FileHelpers
from support import MenuItem
from support import MenuDriven


class TestSupport(TestCase):

    def test_resource_file_pathing(self):
        file_path = os.path.dirname(os.path.realpath(__file__)) 
        file_path = os.path.join(file_path, "resource", "test.txt") 

        assert FileHelpers.default_resource_file_path("test.txt") == file_path


    def test_safe_input(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "test"

            output = Helpers.safe_input("test")
            assert output == "test"

    
    def test_safe_input_keyboard_interupt(self):
        with patch('builtins.input') as handle_input:
            handle_input.side_effect = [KeyboardInterrupt]

            with self.assertRaises(SystemExit):
                Helpers.safe_input("test")


    def test_safe_input_eof_error(self):
        with patch('builtins.input') as handle_input:
            handle_input.side_effect = [EOFError]

            with self.assertRaises(SystemExit):
                Helpers.safe_input("test")


    def test_write_file_string(self):
        open_mock = mock.mock_open()
        with patch("builtins.open", open_mock, create=True):
            FileHelpers.write_file("./test.txt", "stuff in a box")
            open_mock.assert_any_call("./test.txt", "w")
            open_mock().write.assert_any_call("stuff in a box")

    
    def test_write_file_list(self):
        open_mock = mock.mock_open()
        with patch("builtins.open", open_mock, create=True):
            FileHelpers.write_file("./test.csv", ["stuff", "in", "a", "box"])
            open_mock.assert_any_call("./test.csv", "w")
            open_mock().writelines.assert_any_call(["stuff", "in", "a", "box"])


    def test_get_user_output_existing_dir(self):
        with patch("os.path.exists") as pathy:
            pathy.return_value = True
            
            with patch('builtins.input') as handle_input:
                handle_input.return_value = "./lel/"

                return_dir = FileHelpers.get_user_output_path()
                assert return_dir == "./lel/"


    def test_get_user_output_nonexisting_dir_create(self):
        with patch("os.path.exists") as pathy:
            pathy.return_value = False
            
            with patch('builtins.input') as handle_input:
                handle_input.side_effect = ["./lel/", "yEs"]

                with patch("os.makedirs"):
                    return_dir = FileHelpers.get_user_output_path()
                    assert return_dir == "./lel/"


    def test_get_user_output_nonexisting_dir_do_not_create(self):
        with patch("os.path.exists") as pathy:
            pathy.return_value = False
            
            with patch('builtins.input') as handle_input:
                handle_input.side_effect = ["./lel/", "no"]

                return_dir = FileHelpers.get_user_output_path()
                
                assert return_dir == tempfile.gettempdir()


    def test_get_user_output_nonexisting_dir_invalid_choice(self):
        with patch("os.path.exists") as pathy:
            pathy.return_value = False
            
            with patch('builtins.input') as handle_input:
                handle_input.side_effect = ["./lel/", "yee", "no"]

                return_dir = FileHelpers.get_user_output_path()
                
                assert return_dir == tempfile.gettempdir()
