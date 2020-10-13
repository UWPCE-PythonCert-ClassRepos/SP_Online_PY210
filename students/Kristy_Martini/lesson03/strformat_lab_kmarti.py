def task_one(a_tuple):
    str0 = str(a_tuple[0]).rjust(3,'0')
    str1 = '{0:8.2f}'.format(a_tuple[1])
    str2 = '{0:.2e}'.format(a_tuple[2])
    str3 = '{0:.3e}'.format(a_tuple[3]) 
    task_one_str = 'file_{} : {}, {}, {}'.format(str0, str1, str2, str3)
    print(task_one_str)
    return task_one_str

def task_two(a_tuple):
    str0 = str(a_tuple[0]).rjust(3,'0')
    str1 = '{0:8.2f}'.format(a_tuple[1])
    str2 = '{0:.2e}'.format(a_tuple[2])
    str3 = '{0:.3e}'.format(a_tuple[3]) 
    task_two_str = f'file_{str0} : {str1}, {str2}, {str3}'
    print(task_two_str)
    return task_two_str

def task_three(a_tuple):
    num_values = len(a_tuple)
    task_three_str = ('the {} numbers are: ' +", ".join(["{}"] * num_values)).format(num_values, *a_tuple)
    print(task_three_str)
    return(task_three)

def task_four(b_tuple):
    str0 = str(b_tuple[3]).rjust(2,'0')
    str3 = str(b_tuple[0]).rjust(2,'0')
    task_four_str = f'{str0} {b_tuple[4]} {b_tuple[2]} {str3} {b_tuple[1]}'
    print(task_four_str)
    return task_four_str

def task_five(c_list):
    # task_five_str = f'The weight of an {c_list[0][:-1]} is {c_list[1]} and the weight of a {c_list[2][:-1]} is {c_list[3]}'
    task_five_str = f'The weight of an {c_list[0][:-1].upper()} is {c_list[1]*1.2} and the weight of a {c_list[2][:-1].upper()} is {c_list[3]*1.2}'
    print(task_five_str)

def task_six(list_tuples):
    print(('Name'.ljust(9,' ')), ('Age'.ljust(4,' ')), ('Cost'.ljust(8,' ')))
    for entry in list_tuples:
        name = entry[0].ljust(10,' ')
        age = str(entry[1]).ljust(5, ' ')
        cost = '$' + str(entry[2]).ljust(8, ' ')
        print(f'{name}{age}{cost}')

    #Extra Task
    ten_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    task_tuple_string = ("".join(["{:<5.0f}"] * len(ten_tuple))).format(*ten_tuple)
    print(task_tuple_string)

if __name__ == "__main__":
    a_tuple = (2, 123.4567, 10000, 12345.67)
    b_tuple = (4, 30, 2017, 2, 27)
    c_list = ['oranges', 1.3, 'lemons', 1.1]
    d_tuple = ('Kristy', 25, 100)
    e_tuple = ('Matt', 26, 1800)
    f_tuple = ('Katie', 25, 14000)
    list_tuples = [d_tuple, e_tuple, f_tuple]
    task_one(a_tuple)
    task_two(a_tuple)
    task_three(a_tuple)
    task_four(b_tuple)
    task_five(c_list)
    task_six(list_tuples)