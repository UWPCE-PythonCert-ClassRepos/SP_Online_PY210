#Format the four element tuple as guided in the exercise.
in_tuple=(2, 123.4567, 10000, 12345.67)
print('file_{:03} :    {}, {:.2E}, {:.3}'.format(in_tuple[0], round(in_tuple[1],2), in_tuple[2], in_tuple[3]))

#Dynamically format a string to take any number of values
def formatter(in_tuple):
    dyn_string = str(in_tuple[0])
    for i in range(1,len(in_tuple)):
        dyn_string = dyn_string + ', ' + str(in_tuple[i])
    form_string = 'the ' + str(len(in_tuple)) + ' numbers are: ' + dyn_string

    return form_string.format(*in_tuple)

#Given a 5 element tuple, print in format as guided by the exercise
def five_formatter(in_tuple):
    form_string = '{:02} {:02} {:04} {:02} {:02}'
    return  form_string.format(in_tuple[3], in_tuple[4], in_tuple[2], in_tuple[0], in_tuple[1])

#Use an f-string to describe the weight of fruit. Do it again but with 20% weight increase.
def weight(in_tuple):
    return f'The weight of an {in_tuple[0][:-1].upper()} is {in_tuple[1]*1.2} and the weight of a {in_tuple[2][:-1].upper()} is {in_tuple[3]*1.2}'

#Format a table with name, age and cost.
def table_fx(in_list):
    #Reference list
    l = [['Johnny', 5, 3.50], ['Bethanie', 10, 42], ['Jacob', 56, 87.99], ['Warren', 101, 1004.56]]
    form_string = '{:10} {:4} {:8.2f}'
    for person in (in_list):
        print (form_string.format(*person))

#Print ten numbers in columns 5 characters wide. Do it in one short line.
numbers_tuple = (1,2,3,4,5,6,7,8,9,10)
print(('{:5}' * len(numbers_tuple)).format(*numbers_tuple))