##################################################
# Task One
##################################################
t = (2, 123.4567, 10000, 12345.67)
print('\''+'file_'+str(t[0]).rjust(3,'0')+' :  ', ''.join(str(round(t[1],2)))+',',''.join(str("{:.2e}".format(t[2])))+',',''.join(str("{:.2e}".format(t[3])))+'\'')

##################################################
# Task Two
##################################################
str1 = 'file_'+str(t[0]).rjust(3,'0')
str2 = str(round(t[1],2))
str3 = str("{:.2e}".format(t[2]))
str4 = str("{:.2e}".format(t[3]))
print(f'\'{str1} :   {str2}, {str3}, {str4}\'')

##################################################
# Task Three
##################################################

def formatter(t):
    s = ("The {} numbers are: "+", ".join(["{}"]*len(t))).format(len(t),*t)
    return s

print(formatter((2,3,5,7,9)))

##################################################
# Task Four
##################################################

t1 = (4, 30, 2017, 2, 27)
print("\'" + str(t1[3]).zfill(2) + " "+ str(t1[len(t1)-1]) +" "+str(t1[2])+" "+str(t1[0]).zfill(2)+" "+str(t1[1])+"\'")

##################################################
# Task Five
##################################################

a = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {a[0]} is {a[1]} and the weight of a {a[2]} is {a[3]}')

##################################################
# Task Six
##################################################
# dictionary with varying cost lengths
d = {
    'Adam': [24, 100],
    'Brian': [20, 1000],
    'Victor': [23, 10000],
     }

for k,v in d.items():
    print(k.ljust(10, " "), str(v[0]).ljust(4," "), str(v[1]).ljust(6," "))

#print a tuple of 10 consecutive numbers in sequence that are 5 characters wide
#filled with whitespace
print(''.join(str(x).ljust(5, " ") for x in range(1,11)))
