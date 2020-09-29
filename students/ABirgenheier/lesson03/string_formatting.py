# import os
# filename = os.path.basename(__file__)
tups = (3, 123.123123, 100000, 9929.01)


print("Task One: >>>")
print('file_{:03d} :    {:.2f}, {:.2e}, {:.2e}\n'.format(
    tups[0], tups[1], tups[2], tups[3]))
print("Task Two: >>>")
print(f'file_{tups[0]:03d} :    {tups[1]:.2f}, {tups[2]:.2e}, {tups[3]:.2e}\n')


print("Task Three: >>>")


def formatter(in_tuple):
    form_string = 'The ' + str(len(in_tuple)) + ' numbers are: {:d}'
    for tup in range(len(in_tuple)-1):
        form_string += ', {:d}\n'
    return form_string.format(*in_tuple)


print("Task Four: >>>")
print(f'file_{tups[0]:03d} :    {tups[1]:.2f}, {tups[2]:.2e}, {tups[3]:.2e}\n')
task_four_tuples = (4, 30, 2017, 2, 27)
print('{3:02d}, {4:02d}, {2:02d}, {0:02d}, {1:02d}\n'.format(*task_four_tuples))

print("Task Five: >>>")
task_five_dict = ['oranges', 1.3, 'lemons', 1.1]
print(
    f'The weight of an {task_five_dict[0][:-1]} is {task_five_dict[1]} and the weight of a {task_five_dict[2][:-1]} is {task_five_dict[3]}.')
print(
    f'The weight of an {task_five_dict[0][:-1].upper()} is {task_five_dict[1]*1.2} and the weight of a {task_five_dict[2][:-1].upper()} is {task_five_dict[3]*1.2}.\n')


print("Task Six: >>>")
print('{:<15}{:<10}{:<9}'.format('name', 'age', 'cost'))
print('{:<15}{:<10}{:<7.2f}'.format('Sylvester', 49, 584.84))
print('{:<15}{:<10}{:<7.2f}'.format('Forest', 6, 435537.9145))
print('{:<15}{:<10}{:<7.2f}\n'.format('Park Bench', 34, 3814.11))

print("Task Six (extra): >>>")
tups = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:<5}' * len(tups)).format(*tups))
