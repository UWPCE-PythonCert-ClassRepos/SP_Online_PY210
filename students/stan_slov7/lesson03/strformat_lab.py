#!/usr/bin/env python3


#-------------------------------Task 1-------------------------------

tup1 = (2, 123.4567, 10000, 12345.67)

fmtstr1 = "file_{:03d} : {:>8.2f}, {:.2e}, {:.2e}".format(*tup1)

print()
print(fmtstr1)

print()
print("--------------------------End of Task 1--------------------------")
print()


#-------------------------------Task 2-------------------------------

#repeating above task now using fstrings:
#using keywords to pass to the f-string with the formatting premade individually 

paddedZeros = "{:03d}".format(tup1[0])
roundedFloat = round(tup1[1], 2)
expDec = "{:.2e}".format(tup1[2])
expSigFig = "{:.2e}".format(tup1[3])

fmtstr2 = f"file_{paddedZeros} :   {roundedFloat}, {expDec}, {expSigFig}"
print(fmtstr2)

print()
print("--------------------------End of Task 2--------------------------")
print()


#-------------------------------Task 3-------------------------------

#in simpler few lines using .join() method instead of loops or enumeration which would be less efficient
def formatter(in_tup):
   len_tup = len(in_tup)
   fmtstr3 = "the {:d} numbers are: " + ", ".join(["{:d}"] *len_tup)
   return fmtstr3.format(len_tup, *in_tup)

#test formatter
tup3 = (1, 2, 3, 4, 5, 6, 7)

print(formatter(tup3))

print()
print("--------------------------End of Task 3--------------------------")
print()


#-------------------------------Task 4-------------------------------

tup4 = (4, 30, 2017, 2, 27)

#simplified changing the positions within the string itself while reading in the tuple in its usual order
fmtstr4 = "{3:02d} {4:d} {2:d} {0:02d} {1:d}".format(*tup4)
print(fmtstr4)

print()
print("--------------------------End of Task 4--------------------------")
print()


