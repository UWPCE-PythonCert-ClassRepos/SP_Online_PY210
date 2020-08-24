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


#-------------------------------Task 5-------------------------------

lst5 = ['oranges', 1.3, 'lemons', 1.1]

#write an f-string to display:
#The weight of an orange is 1.3 and the weight of a lemon is 1.1

fruit1 = lst5[0][:-1] 
fruit2 = lst5[2][:-1]
weight1 = lst5[1]
weight2 = lst5[3]

#pass these names to the fstrings and modify them however needed later
fstr1 = f"The weight of an {fruit1} is {weight1} and the weight of a {fruit2} is {weight2}" 
print(fstr1)
print()

print("Now change to display the fruits names in uppercase and their weights increased by 20%...")
print()

#f-strings allow to pass functions or do math within the { } in the template string itself
fstr2 = f"The weight of an {fruit1.upper()} is {weight1*1.2} and the weight of a {fruit2.upper()} is {weight2*1.2}" 
print(fstr2)

print()
print("--------------------------End of Task 5--------------------------")
print()


#-------------------------------Task 6-------------------------------

#print several rows of alligned collumns, each containing a name, age, cost 

data = [("Joe", 33, 1800.89),
        ("Rebecca", 27, 12000),
        ("Kenny", 28, 9700.79),
        ("Alexa", 31, 340000),
        ("Rob", 37, 357.37)]

hdr = "| Name:       |  Age:  |   Cost:    |"
spr = "+" + ("-"*13) + "+" + ("-"*8) + "+" + ("-"*12) + "+"
row = "| {name:<12s}|{age:^8d}|${cost:>10.2f} |".format

print(spr)
print(hdr)
print(spr)
for person in data:
    print(row(name = person[0], age = person[1], cost = person[2]))
print(spr)

print()
print("--------------------------End of Task 6--------------------------")
print()


#------------Extra Task------------ 

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
length = len(nums)
border =  ("+" + ("-"*5)) * length + "+"

#have two sets of { } brackets inside the {:d} containing the tuple values
#so that they can be setup to be able to change the fill and width of the columns

style = ("|{:^{fill}{width}d}" * length + "|").format

print(border)
print(style(*nums, fill = "", width = 5))
print(border)

print()
print("--------------------------End of Extra Task--------------------------")
print()