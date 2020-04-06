#!/usr/bin/env python3
'''string formatting exercises for Gerry Gabrisch'''


###   task 1
print('task 1'+ '\n')
#a barely human-readable sting formatting exercise using f strings.
i = (2, 123.4567, 10000, 12345.67)
newstring ="file_" + f"{i[0]:0=3}"+ ' :' + f"{' ':2}" + f"{i[1]:.2f}"+ ', '+ f"{i[2]:.2e}"+ ', '+f"{i[3]:.2e}"
print(newstring)


###   task 2
print('\n''task 2'+ '\n')
#a barely human-readable sting formatting exercise using .format() .
newstring = "file_" +  "{:0=3}".format(i[0]) + " :" +"{:2}".format(' ') + "{:.2f}".format(i[1]) + ", "+  "{:.2e}".format(i[2]) + ", " + "{:.2e}".format(i[3])
print(newstring)


###   task 3
print('\n''task 3'+ '\n')
# a tuple of numbers
t = (1,)
def format_a_matic(t):
    '''take a tuple of any length and return a formatted string for each tuple element...'''
    #make a formater based on the number of tuple elements
    formats = '{:d}, ' * len(t)
    #strip out the last comma and blank space when done...
    formats = formats.rstrip(', ')
    #in case the tuple is empty do this...
    if len(t) == 0:
        return "No formatting possible on an empty tuple, sorry to disappoint you..."
    #if the tuple length is 1 then alter the English statement...
    if len(t) == 1:
        numbernumbers = " number is : "
    else:
        numbernumbers = " numbers are : "
        
    return "the " + str(len(t)) + numbernumbers + formats.format(*t)
print(format_a_matic(t))

###    task 4
print('\n''task 4'+ '\n')
t = ( 4, 30, 2017, 2, 27)
print(f'{t[3]:0=2}, {t[4]}, {t[2]},{t[0]:0=2},{t[1]}')

###   task 5
print('\n''task 5'+ '\n')
t= ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {t[0][:-1]} is {t[1]} and the weight of a {t[2][:-1]} is {t[3]}.")

print(f"The weight of an {t[0][:-1].upper()} is {t[1]*1.2} and the weight of a {t[2][:-1].upper()} is {t[3]*1.2}.")

###   task 6
print('\n''task 6'+ '\n')
Ids = ('name', 'age', 'cost')
whiskey = ('Gerragoofin', 20, 120.95)
wine = ('Chateau Margaux', 233, 225000)
car = ('Lamborghini Venino', 6, 4500000)
gum = ('Trident', 0, 1.45)

print(f"{Ids[0]:<20} {Ids[1]:>5} {Ids[2]:>20}")
print(f"{whiskey[0]:<20} {whiskey[1]:>5} {f'${whiskey[2]:.2f}':>20}")
print(f"{wine[0]:<20} {wine[1]:>5} {f'${wine[2]:.2f}':>20}")
print(f"{car[0]:<20} {car[1]:>5} {f'${car[2]:.2f}':>20}")
print(f"{gum[0]:<20} {gum[1]:>5} {f'${gum[2]:.2f}':>20}")

print()
t =(1,2,3,4,5,6,7,8,9,10)
#this works with a .format style but I could not make it work with f strings.  Any hints?
print(('{:5}\n'*10).format(*t))