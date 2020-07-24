#!/usr/bin/env python3

"""
Lesson 3: String Format Lab
Course: UW PY210
Author: Jason Jenkins
"""


def formatString_1(fileNum, floatNum1, intNum, floatNum2):
    """
    Task 1
    Format the string

    :param fileNum: value a filenumber
    :param floatNum1: display it with 2 decimal places
    :param intNum: display in scientific notation, with 2 decimal places
    :param floatNum2: display in scientific notation with 3 sig fig
    """

    text = "file_{:0>3d} :{:9.2f}, {:.2e}, {:.3g}"
    result = text.format(fileNum, floatNum1, intNum, floatNum2)
    print(result)
    return result


def formatString_2(fileNum, floatNum1, intNum, floatNum2):
    """
    Task 2
    Format the string

    :param fileNum: value a filenumber
    :param floatNum1: display it with 2 decimal places
    :param intNum: display in scientific notation, with 2 decimal places
    :param floatNum2: display in scientific notation with 3 sig fig
    """

    result = f"file_{fileNum:0>3d} :{floatNum1:9.2f}, {intNum:.2e}, {floatNum2:.3g}"
    print(result)
    return result


def formatString_3(*tmpTuple):
    """
    Rewrite a tumpe to the following
    the {total items} numbers are: {num1}, {num2}, ...

    :param tmpTuple: tuple to be converted to string
    """

    totalItems = len(tmpTuple)
    formated_string = "the {} numbers are: "
    formated_string += ", ".join(["{}"] * totalItems)
    result = formated_string.format(totalItems, *tmpTuple)

    print(result)
    return result


def formatString_4(*tmpTuple):
    """
    Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
    use string formating to print: '02 27 2017 04 30'

    :param tmpTuple: tuple to be converted to string
    """

    result = f"{tmpTuple[3]:0>2d} {tmpTuple[4]:0>2d} "
    result += f"{tmpTuple[2]:0>4d} {tmpTuple[0]:0>2d} "
    result += f"{tmpTuple[1]:0>2d}"

    print(result)
    return result


def formatString_5(tmpList=[]):
    """
    Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display:
    The weight of an orange is 1.3 and the weight of a lemon is 1.1

    but change to display the names of the fruit in upper case,
    and the weight 20% higher (that is 1.2 times higher)

    :param tmpList: list to be converted to string
    """

    result = f"The weight of an {tmpList[0][:-1].upper()} is {tmpList[1] * 1.2} and "
    result += f"the weight of a {tmpList[2][:-1].upper()} is {tmpList[3] * 1.2}"

    print(result)
    return result


def formatString_6(*tmpTuple):
    """
    Part 1:
    Print a table of several rows, each with a name, an age and a cost.
    Make sure some of the costs are in the hundreds and thousands to test
    your alignment specifiers.

    Part 2:
    Given a tuple with 10 consecutive numbers,
    can you work how to quickly print the tuple in columns that are 5
    charaters wide?

    :param tmpList: list to be converted to string
    """

    Col1 = "Name"
    Col2 = "Age"
    Col3 = "Cost"

    # Part 1
    basicBurbon = ["BasicBurbon", "5", "25"]
    niceBurbon = ["NiceBurbon", "20", "213"]
    wowBurbon = ["WowBurbon", "123", "2353"]
    oldBurbon = ["oldBurbon", "1323", "23135"]

    result = f"{Col1:20} {Col2:10} {Col3:10}\n"
    result += f"{basicBurbon[0]:20} {basicBurbon[1]:10} {basicBurbon[2]:10}\n"
    result += f"{niceBurbon[0]:20} {niceBurbon[1]:10} {niceBurbon[2]:10}\n"
    result += f"{wowBurbon[0]:20} {wowBurbon[1]:10} {wowBurbon[2]:10}\n"
    result += f"{oldBurbon[0]:20} {oldBurbon[1]:10} {oldBurbon[2]:10}\n"

    print(result)

    # Part 2 (Couldn't figure out how to do if using f"")
    print("".join(["{:5}"] * len(tmpTuple)).format(*tmpTuple))


if __name__ == "__main__":
    # testing
    result = formatString_1(2, 123.4567, 10000, 12345.67)
    assert result == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    result = formatString_1(53, 1233.464327, 1012432000, 153345.6417)
    assert result == 'file_053 :  1233.46, 1.01e+09, 1.53e+05'

    result = formatString_2(2, 123.4567, 10000, 12345.67)
    assert result == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    result = formatString_2(53, 1233.464327, 1012432000, 153345.6417)
    assert result == 'file_053 :  1233.46, 1.01e+09, 1.53e+05'

    assert formatString_3(2, 3, 5) == 'the 3 numbers are: 2, 3, 5'
    assert formatString_3(2, 3, 5, 7, 9) == 'the 5 numbers are: 2, 3, 5, 7, 9'

    assert formatString_4(4, 30, 2017, 2, 27) == '02 27 2017 04 30'

    result = formatString_5(['oranges', 1.3, 'lemons', 1.1])
    expected = "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"
    assert result == expected

    formatString_6(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    formatString_6(1, 2, 3, 4)

    print()
    print("All Tests Pass")
