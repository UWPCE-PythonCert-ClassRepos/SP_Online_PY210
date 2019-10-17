# TASK ONE
def string_format(user_input):
    file_name = "file_" + "0" * (3 - len(str(user_input[0]))) + str(user_input[0])

    last_num = (str(user_input[1]).index(".") + 3)
    second_val = str(user_input[1])[0:last_num]

    def sci_note(num_str, sig_fig):
        first_num = num_str[0]
        next_two = num_str[1:3]
        place_count = len(num_str[1:])
        result = first_num + "." + next_two + "e+" + ("0" * (sig_fig - place_count)) + str(place_count)
        return result

    third_val = sci_note(str(user_input[2]), 2)

    fourth_val = sci_note(str(user_input[3]), 3)

    print(file_name + " :   " + second_val + ", " + third_val + ", " + fourth_val)


# TASK TWO
def string_format2(user_input):
    file_name = "file_" + "0" * (3 - len(str(user_input[0]))) + str(user_input[0])

    last_num = (str(user_input[1]).index(".") + 3)
    second_val = str(user_input[1])[0:last_num]

    def sci_note(num_str, sig_fig):
        first_num = num_str[0]
        next_two = num_str[1:3]
        place_count = len(num_str[1:])
        result = first_num + "." + next_two + "e+" + ("0" * (sig_fig - place_count)) + str(place_count)
        return result

    third_val = sci_note(str(user_input[2]), 2)

    fourth_val = sci_note(str(user_input[3]), 3)

    print('{} :   {}, {}, {}'.format(file_name, second_val, third_val, fourth_val))


# TASK THREE
def string_task3(user_input):
    input_len = len(user_input)
    num_list = ', '.join(['{:d}'] * input_len)
    result = 'the {:d} numbers are: ' + num_list
    print(result.format(input_len, *user_input))


# TASK FOUR
def string_task4(user_input):
    result = '{3:02} {4:02} {2:02} {0:02} {1:02}'.format(*user_input)

    print(result)


# TASK FIVE
def string_task5(user_input):
    fruit1 = user_input[0]
    fruit2 = user_input[2]
    weight1 = user_input[1]
    weight2 = user_input[3]

    result = f'The weight of an {fruit1} is {weight1 * 1.2} and the weight of a {fruit2} is {weight2 * 1.2}'

    print(result)


# TASK SIX
def string_task6():
    format_string = '{:10}{:>10}{:>10}'
    print(format_string.format('Name', 'Age', 'Cost'))
    print(format_string.format('Mike', '32', '193.95'))
    print(format_string.format('Jill', '13', '12.36'))
    print(format_string.format('Angela', '53', '4923.17'))
    print(format_string.format('Dilbert', '46', '39332.20'))

