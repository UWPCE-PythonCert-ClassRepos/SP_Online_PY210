#Task 1
#Create tuple with given data
Four_Elem_tuple = (2, 123.4567, 10000, 12345.67)

#format tuple. d = double, f = floating point, e = scientfic notation.
#Need a '*' to unpack the tuple into arguments
print("file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(*Four_Elem_tuple))

#Task 2

#Use tuple from task 1

print(f"file_{Four_Elem_tuple[0]:0>3d} :   {Four_Elem_tuple[1]:.2f}, {Four_Elem_tuple[2]:.2e}, {Four_Elem_tuple[3]:.2e}")

#Task 3
#Format a tuple with an aribitrary number of arguments into a string


def Arb_Tup_Str(tuple):
    #initialize tuple
    n = len(tuple)
    #create a string that includes formating for the number of entries
    num_ent = "{:d}" + ", {:d}"*(n-1)
    #format num_ent with the tuple
    Numbers = num_ent.format(*tuple)
    #add numbers to full formatted sentence
    return f"the {n} numbers are: {Numbers}"

#Test on a random tuple of numbers  
t = (3,4,5,6,7,8,9)
print(Arb_Tup_Str(t))

#Task 4
#create tuple
a,b,c,d,e = (4, 30, 2017, 2, 27)
#Format inputs in specific order and styles
print(f"{d:0>2d} {e} {c} {a:0>2d} {b}")


#Task 5
#Create list 
List = ['oranges', 1.3, 'lemons', 1.1]

#format string. Truncate the fruits to remove the plural
print(f"The weight of an {List[0]:.6} is {List[1]} and the weight of a {List[2]:.5} is {List[3]}")

#Same thing as above but upper case fruit and increase the weight by multiplying the input 
print(f"The weight of an {List[0].title():.6} is {List[1]*1.2} and the weight of a {List[2].title():.5} is {List[3]*1.2}")

#Task 6
#Column Headers
headers = ('Name', 'Age', 'Cost')
#Print headers. Centerened because it looks nice
print(f"{headers[0]:^20}{headers[1]:^6}{headers[2]:^12}")
#Create random inputs for the three columns
r1 = ("John Smith", "439", "$101010.00")
r2 = ("John Rambo", "72", "$0.01")
r3 = ("Joan of arcward", "605", "$857.89")
r4 = ("Jonathan Van Ness", "32", "$16.50")
Rows = [r1, r2, r3, r4]
#Align each row
for n in Rows:
    print(f"{n[0]:>20}{n[1]:>6}{n[2]:>12}")


#Bonus Task
a,b,c,d,e,f,g,h,i,j = (1,2,3,4,5,6,7,8,9,10)
print(f"{a:5}{b:5}{c:5}{d:5}{e:5}{f:5}{g:5}{h:5}{i:5}{j:5}")
