def count_evens(number_list):
    count = 0
    for number in number_list:
        if number % 2 == 0:
            count += 1
    return count

