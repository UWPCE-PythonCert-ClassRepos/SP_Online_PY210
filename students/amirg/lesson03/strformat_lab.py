'''Task one prints a four element tuple'''
def task_one(fnames):
    print('file_00{} : {:.2f}, {:.2e}, {:.2e}'.format(*fnames))
'''Same as task one using alternative formatting'''
def task_two(fnames):
    print('file_00%d : %.2f, %.2e, %.2e' % fnames)
'''Dynamically formatting a tuple for any size of tuple'''
def formatter(in_tuple):
    form_string = 'the {:d} numbers are:'.format(len(in_tuple))
    for i in range(len(in_tuple)):
        form_string += ' {:d}'
        if i != len(in_tuple)-1:
            form_string += ','
    return form_string.format(*in_tuple)
'''Outputting a re-arranged tuple'''
def task_four(fnames):
    print('0{:d} {:d} {:d} 0{:d} {:d}'.format(fnames[3], fnames[4], fnames[2], fnames[0], fnames[1]))
'''Outputting a tuple using f-string'''
def task_five(fnames):
    print(f'The weight of an {fnames[0].upper()} is {fnames[1]*1.2} and the weight of a {fnames[2].upper()} is {fnames[3]*1.2}')
'''Outputs formatted rows of data and 5 character wide columns for consecutive numbers'''
def task_six():
    align = '{:^10}'
    new = '\n'
    print(align.format('Bob') + align.format('24') + align.format('$100'))
    print(align.format('Chris') + align.format('26') + align.format('$100,000'))
    print(align.format('Rob') + align.format('35') + align.format('$10,000,000'))
    align2 = '{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}'
    print(align2.format('10', '11', '12', '13', '14', '15', '16', '17', '18', '19'))