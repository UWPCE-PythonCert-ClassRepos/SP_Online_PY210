def string_bits(str):
    number_of_letters = len(str)
    odd_str = ''
    for i in range(number_of_letters):
        if i % 2 == 0:
            odd_str = odd_str + str[i]
    return odd_str