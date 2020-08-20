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


