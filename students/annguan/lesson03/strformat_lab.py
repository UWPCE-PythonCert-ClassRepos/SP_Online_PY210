#Lesson 3 String Formatting Lab Exercise

##Task One
"""a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""

print("file_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))
print()

##Task Two
"""alternative method to achieve task one"""
t1 = (2, 123.4567, 10000, 12345.67)
print(f"file_{t1[0]:0>3d} :   {t1[1]:.2f}, {t1[2]:.2e}, {t1[3]:.3e}")

##Task Three
def formatter(in_tuple):
"""print out arbitrary length tuples"""
    t3 = "the {} numbers are: ".format(len(in_tuple))

    if len(in_tuple) > 0:
        t3 += "{}".format(in_tuple[0]);

    for num in in_tuple[1:]:
        t3 += ", {}".format(num)

    return t3

##Task Four
"""given a 5 element tuple - t4; print in specified order"""
t4 = (4, 30, 2017, 2, 27)
print("{n3:0>2d} {n4:0>2d} {n2:0>2d} {n0:0>2d} {n1:0>2d}".format(
        n0=t4[0], n1=t4[1], n2=t4[2], n3=t4[3], n4=t4[4]))

##Task Five
"""Given ['oranges', 1.3, 'lemons', 1.1], use f-string to print The weight of an orange is 1.3 and the weight of a lemon is 1.1
and change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher)"""
orange = ("orange", 1.3)
lemon = ("lemon",1.1)

print(f"The weight of an {orange[0]} is {orange[1]} and the weight of a {lemon[0]} is {lemon[1]}")
print(f"The weight of an {orange[0].upper()} is {orange[1] * 1.2} and the weight of a {lemon[0].upper()} is {lemon[1] * 1.2}")

##Task Six
"""name, age, cost"""
t6 = list()
t6.append(("Ann", 16, 154367))
t6.append(("Selvan", 33, 235))
t6.append(("Bunny", 5, 5678))
t6.append(("Kelly", 7, 2346))

for i in t6:
    print("{:<20}  {:>3d}  ${:>15.2f}".format(*d))

"""extra task: given a tuple with 10 consecutive numbers, print tuple in columns that are 5 char wide"""
print(' '.join(('%*s' % (5, i) for i in range(10))))



