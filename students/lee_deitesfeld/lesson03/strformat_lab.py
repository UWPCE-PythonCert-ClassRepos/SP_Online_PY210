#Task One - Write a format string that will take a tuple and turn it into 'file_002 : 123.46, 1.00e+04, 1.23e+04'
nums = 'file_%03d :  %.2f, %.2E, %.2E' % (2, 123.4567, 10000, 12345.67)
print(nums)

#Task Two
def f_string(name, color, ice_cream):
    '''Takes three arguments and inserts them into a format string'''
    favorite = f"My name is {name}. My favorite color is {color}, and my favorite ice cream flavor is {ice_cream}."
    print(favorite)

#Task Three
def formatter(seq):
    '''Writes a function that displays "The __ numbers are: __, __, etc" '''
    length = len(seq)
    print(("The {} numbers are: " + ", ".join(["{}"] * length)).format(length, *seq))

#Task Four
def num_pad(seq):
    '''Converts (4, 30, 2017, 2, 27) to "02 27 2017 04 30" '''
    lst = []
    #return nums in sequence padded with zeroes
    for num in seq:
        lst.append(f'{num:02}')
    #convert list to string with no commas
    first_str = (' '.join(lst))
    first = first_str[0:6]
    middle = first_str[6:11]
    last = first_str[11:]
    #print final string
    print(last + ' ' + middle + first)

#Task Five - Display 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
fruits = ['oranges', 1.3, 'lemons', 1.1]
f_str = f'The weight of an {(fruits[0])[:-1]} is {fruits[1]} and the weight of a {(fruits[2])[:-1]} is {fruits[3]}.'
print(f_str)
#Then, display the names of the fruit in upper case, and the weight 20% higher
f_str_bonus = f'The weight of an {((fruits[0])[:-1]).upper()} is {fruits[1]*1.2} and the weight of a {((fruits[2])[:-1]).upper()} is {fruits[3]*1.2}.'
print(f_str_bonus)

#Task Six - print a table of several rows, each with a name, an age and a cost
for line in [["Name", "Age", "Cost"], ["Lee", 33, "$56.99"], ["Bob", 62, "$560.99"], ["Harry", 105, "$5600.99"], ["Jeanne", 99, "$56099.99"]]:
    print('{:>8} {:>8} {:>8}'.format(*line))
#Then, given a tuple with 10 consecutive numbers, print the tuple in columns that are 5 charaters wide
tup = (1,2,3,4,5,6,7,8,9,10)
for x in tup:
    print('{:>5}'.format(x), end= " ")
