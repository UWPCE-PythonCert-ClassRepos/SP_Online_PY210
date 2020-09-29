

# Task One
string = ( 2, 123.4567, 10000, 12345.67)
string_formated = "file_{:03d} : {:10.2f}, {:.2e}, {:.2e}".format(string[0], string[1], string[2], string[3])
print(string)
print(string_formated)

# Task Two 
string_alternative = f"file_{string[0]:0>3d} :   {string[1]:.2f}, {string[2]:.2e}, {string[3]:.2e}"
print(string_alternative)


#Task Three
def formatter(in_tuple):
    size = len(in_tuple)
    format_string = ", ".join(["{}"]*size)
    return ("'"+"The {} numbers are: "+format_string +"'").format(size, *in_tuple)

num1 = (1,3,6,18)
num2 = (1,4,9,10,14)
print(formatter(num1))
print(formatter(num2))


# Task Four
num = (4, 30, 2017, 2, 27)
print("{3:0>2d} {4:0} {2:0} {0:0>2d} {1:0}".format(*num))

# Task Five
string = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {string[0][:-1]} is {string[1]} and the weight of a {string[2][:-1]} is {string[3]}")
print(f"The weight of an {string[0][:-1].upper()} is {string[1]*1.2} and the weight of a {string[2][:-1].upper()} is {string[3]*1.2}")


# Task Six
# Print a table with a name, an age and a cost
data = list()
data.append(("Pushkin", 37, 9000))
data.append(("Lermontov", 41, 2000))
data.append(("Tolstoy", 65, 90000))
data.append(("Dostoevsky", 57, 5800))
for row in data:
    print('{:<20}{:<4}{:>15.{d}f}'.format(*row, d=2))
    
# Print 10 consecutive numbers with 5 character wide 
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:{wide}}'*len(num)).format(*num, wide=5))   
