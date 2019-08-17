#!/usr/bin/env python3

# ------------------------------ #
# String Lab Assignment for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/9/2019, Created and tested script
# ------------------------------ #

# ----- Task 1 ----- #
myTuple = (2, 123.4567, 10000, 12345.67)
formatted = (f"file_{myTuple[0]:003d} :   {myTuple[1]:.2f}, {myTuple[2]:.2e}, {myTuple[3]:.2e}")
print(formatted)

# ----- Task 2 ----- #
myTuple = (2, 123.4567, 10000, 12345.67)
formatted = ("file_{:003d} :   {:.2f}, {:.2e}, {:.2e}".format(myTuple[0], myTuple[1], myTuple[2], myTuple[3]))
print(formatted)

# ----- Task 3 ----- #
def formatter(myTuple):
    interim ="{:d}"
    if type(myTuple) == int:
        formatted = f"The 1 number is: " + interim
        return formatted.format(myTuple)
    else:
        i = 2
        while i <= len(myTuple):
            interim = interim + ", {:d}"
            i += 1
        formatted = f"The {len(myTuple):d} numbers are: " + interim
        return formatted.format(*myTuple)

# ----- Task 4 ----- #
myTuple = (4, 30, 2017, 2, 27)
formatted = (f"{myTuple[3]:02d} {myTuple[4]:d} {myTuple[2]:d} {myTuple[0]:02d} {myTuple[1]:d}")
print(formatted)

# ----- Task 5 ----- #
myList = ["orange", 1.3, "lemon", 1.1]
print(f"The weight of an {myList[0]:s} is {myList[1]:.1f} and the weight of a {myList[2]:s} is {myList[3]:.1f}")

myList = ["orange", 1.3, "lemon", 1.1]
print(f"The weight of an {myList[0].upper():s} is {myList[1]*1.2:.1f} and the weight of a {myList[2].upper():s} is {myList[3]*1.2:.1f}")

# ----- Task 6 ----- #
myList = [("John", "40", "10,000"), ("Jane", "34", "575"), ("Samantha", "23", "15,575")]

for tpl in myList:
    print("{:<20}{:>3}{:>10}".format(tpl[0], tpl[1], tpl[2]))
