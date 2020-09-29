def task1(seq):
    txt = 'file_{:03d}: {:.2f}, {:.2e}, {:.2e}'.format(*seq)
    return txt

print('task1 result: ', task1(( 2, 123.4567, 10000, 12345.67)))


# task2
def task2(seq):
    txt = f'file_{seq[0]:03d}: {seq[1]:.2f}, {seq[2]:.2e}, {seq[3]:.2e}'
    return txt
print('task2 result: ', task2(( 2, 123.4567, 10000, 12345.67)))

# task3
def formatter(seq):
    text = ('The {} numbers are: ' + ','.join(['{}'] * len(seq))).format(len(seq), *seq)
    return text

t = (1,2,3)
print('task3 result 1: ', formatter(t))
print('task3 result 2: ', formatter(t*2))


# task4
def task4(seq):
    txt = f'{seq[3]:02d} {seq[4]:02d} {seq[2]:02d} {seq[0]:02d} {seq[1]:02d}'
    return txt

print('task4 result: ', task4(( 4, 30, 2017, 2, 27)))

# task5
def task5(lst):
    txt1 = f'The weight of an {lst[0]} is {lst[1]} and the weight of a {lst[2]} is {lst[3]}'
    txt2 = f'The weight of an {lst[0].upper()} is {lst[1] * 1.2} and the weight of a {lst[2].upper()} is {lst[3] * 1.2}'
    return txt1 + '\n' + txt2

print('task5 result: ', task5(['oranges', 1.3, 'lemons', 1.1]))

# task6
people = [['mike', 75.02, '$789.80'], ['sam', 1.6, '$1.09'], ['luis', 900, '$666,666.60']]

def task6(seq):
    print(f"\n\n{'Name':<10}{'Age':<8} {'Cost':<12}")
    print("-" * 9 + " " + "-" * 8 + " " + "-"*11)
    for info in seq:
        print(f"{info[0]:<10}{info[1]:>8}{info[2]:>12}")

task6(people)
