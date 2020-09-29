#UWPCE PY210
#Lesson03, String Formatting Exercise

#Task One
def format_tuple(tup1):
    str_formatted = 'file_{:0>3d} : {:>4}{:.2f}, {:.2e}, {:.2e}'.format(tup1[0],
        "",tup1[1],tup1[2],tup1[3])
    print(str_formatted)

#Task Two
def format_opt2(tup1):
    print(f'file_{tup1[0]:0>3d} :     {tup1[1]:.2f}, {tup1[2]:.2e}, {tup1[3]:.2e}')

#Task Three
def dyn_format(seq):
    count = len(seq)
    str_output = ('the {} numbers are: ' +
    ', '.join(['{:d}'] * count)).format(count,*seq)
    return str_output

#Task Four
def task_four(seq):
    str_output = '{:0>2d} {} {} {:0>2d} {}'.format(seq[3],seq[4],seq[2],seq[0],seq[1])
    return str_output

#Task Five
def task_five(seq):
    str_output = (f'The weight of an {seq[0][0:-1]} is {seq[1]} and the '
                  f'weight of a {seq[2][0:-1]} is {seq[3]}')
    print(str_output)

    str_output2 = (f'The weight of an {seq[0][0:-1].upper()} is {seq[1]*1.2} '
                   f'and the weight of a {seq[2][0:-1].upper()} is {seq[3]*1.2}')
    print(str_output2)

#Task Six
def task_six(seq):
    print(''.join(['{:>5}'] * len(seq)).format(*seq))

def main():
    #Task One
    print('{}Task One{}'.format('-'*4,'-'*4))
    tup_test = ( 2, 123.4567, 10000, 12345.67)
    format_tuple(tup_test)

    #Task Two
    print('{}Task Two{}'.format('-'*4,'-'*4))
    format_opt2(tup_test)

    #Task Three
    print('{}Task Three{}'.format('-'*4,'-'*4))
    tup_test2 = (1,2,3,4)
    tup_test3 = (4, 5, 6, 1, 2)
    print(dyn_format(tup_test2))
    print(dyn_format(tup_test3))

    #Task Four
    print('{}Task Four{}'.format('-'*4,'-'*4))
    tup_test4 = (4, 30, 2017, 2, 27)
    print(task_four(tup_test4))

    #Task Five
    print('{}Task Five{}'.format('-'*4,'-'*4))
    list_test = ['oranges', 1.3, 'lemons', 1.1]
    task_five(list_test)

    #Task Six
    print('{}Task Six{}'.format('-'*4,'-'*4))
    tup_test6 = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
    task_six(tup_test6)

main()