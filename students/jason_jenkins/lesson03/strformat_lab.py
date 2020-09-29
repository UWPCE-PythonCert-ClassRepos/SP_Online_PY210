#!/usr/bin/env python3

"""
Lesson 3: String Format Lab
Course: UW PY210
Author: Jason Jenkins
"""


def format_string_1(file_num, float_num1, int_num, float_num2):
    """
    Task 1
    Format the string

    :param fileNum: value a filenumber
    :param floatNum1: display it with 2 decimal places
    :param intNum: display in scientific notation, with 2 decimal places
    :param floatNum2: display in scientific notation with 3 sig fig
    """

    text = "file_{:0>3d} :{:9.2f}, {:.2e}, {:.3g}"
    result = text.format(file_num, float_num1, int_num, float_num2)
    print(result)
    return result


def format_string_2(file_num, float_num1, int_num, float_num2):
    """
    Task 2
    Format the string

    :param fileNum: value a filenumber
    :param floatNum1: display it with 2 decimal places
    :param intNum: display in scientific notation, with 2 decimal places
    :param floatNum2: display in scientific notation with 3 sig fig
    """

    result = f"file_{file_num:0>3d} :{float_num1:9.2f}, {int_num:.2e}, {float_num2:.3g}"
    print(result)
    return result


def format_string_3(*tmp_tuple):
    """
    Rewrite a tumpe to the following
    the {total items} numbers are: {num1}, {num2}, ...

    :param tmp_tuple: tuple to be converted to string
    """

    total_items = len(tmp_tuple)
    formated_string = "the {} numbers are: "
    formated_string += ", ".join(["{}"] * total_items)
    result = formated_string.format(total_items, *tmp_tuple)

    print(result)
    return result


def format_string_4(*tmp_tuple):
    """
    Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
    use string formating to print: '02 27 2017 04 30'

    :param tmp_tuple: tuple to be converted to string
    """

    result = f"{tmp_tuple[3]:0>2d} {tmp_tuple[4]:0>2d} "
    result += f"{tmp_tuple[2]:0>4d} {tmp_tuple[0]:0>2d} "
    result += f"{tmp_tuple[1]:0>2d}"

    print(result)
    return result


def format_string_5(tmp_list=[]):
    """
    Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display:
    The weight of an orange is 1.3 and the weight of a lemon is 1.1

    but change to display the names of the fruit in upper case,
    and the weight 20% higher (that is 1.2 times higher)

    :param tmp_list: list to be converted to string
    """

    result = f"The weight of an {tmp_list[0][:-1].upper()} is {tmp_list[1] * 1.2} and "
    result += f"the weight of a {tmp_list[2][:-1].upper()} is {tmp_list[3] * 1.2}"

    print(result)
    return result


def format_string_6(*tmp_tuple):
    """
    Part 1:
    Print a table of several rows, each with a name, an age and a cost.
    Make sure some of the costs are in the hundreds and thousands to test
    your alignment specifiers.

    Part 2:
    Given a tuple with 10 consecutive numbers,
    can you work how to quickly print the tuple in columns that are 5
    charaters wide?

    :param tmp_list: list to be converted to string
    """

    col1 = "Name"
    col2 = "Age"
    col3 = "Cost"

    # Part 1
    basic_bourbon = ["Basicbourbon", "5", "25"]
    nice_bourbon = ["Nicebourbon", "20", "213"]
    wow_bourbon = ["Wowbourbon", "123", "2353"]
    old_bourbon = ["oldbourbon", "1323", "23135"]

    result = f"{col1:20} {col2:10} {col3:10}\n"
    result += f"{basic_bourbon[0]:20} {basic_bourbon[1]:10} {basic_bourbon[2]:10}\n"
    result += f"{nice_bourbon[0]:20} {nice_bourbon[1]:10} {nice_bourbon[2]:10}\n"
    result += f"{wow_bourbon[0]:20} {wow_bourbon[1]:10} {wow_bourbon[2]:10}\n"
    result += f"{old_bourbon[0]:20} {old_bourbon[1]:10} {old_bourbon[2]:10}\n"

    print(result)

    # Part 2 (Couldn't figure out how to do if using f"")
    result = "".join(["{:5}"] * len(tmp_tuple)).format(*tmp_tuple)
    print(result)
    return(result)



if __name__ == "__main__":
    # testing
    result = format_string_1(2, 123.4567, 10000, 12345.67)
    assert result == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    result = format_string_1(53, 1233.464327, 1012432000, 153345.6417)
    assert result == 'file_053 :  1233.46, 1.01e+09, 1.53e+05'

    result = format_string_2(2, 123.4567, 10000, 12345.67)
    assert result == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    result = format_string_2(53, 1233.464327, 1012432000, 153345.6417)
    assert result == 'file_053 :  1233.46, 1.01e+09, 1.53e+05'

    assert format_string_3(2, 3, 5) == 'the 3 numbers are: 2, 3, 5'
    assert format_string_3(2, 3, 5, 7, 9) == 'the 5 numbers are: 2, 3, 5, 7, 9'

    assert format_string_4(4, 30, 2017, 2, 27) == '02 27 2017 04 30'

    result = format_string_5(['oranges', 1.3, 'lemons', 1.1])
    expected = "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"
    assert result == expected

    format_string_6(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert format_string_6(1, 11, 111, 1111) == '    1   11  111 1111'

    print()
    print("All Tests Pass")
