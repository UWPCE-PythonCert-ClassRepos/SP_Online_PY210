#Christine Kim
#Python210 Lesson 3 String Formatting Lab Exercise

#Task One

#Given tuple
t1_tuple = (2, 123.4567, 10000, 12345.67)

#d for decimal integer, f for floating point, e for exponent notation, g for significant digits
t1_str = "file_{:03d} :    {:.2f}, {:.2e}, {:.3g}".format(t1_tuple[0], t1_tuple[1], t1_tuple[2], t1_tuple[3])
#Verify result
print(t1_str)

#Task Two
t2_tuple = t1_tuple

t2_str = f"file_{t2_tuple[0]:03d} :    {t2_tuple[1]:.2f}, {t2_tuple[2]:.2e}, {t2_tuple[3]:.3g}"
print(t2_str)

#Task Three
t3 = (2, 3, 5, 7, 9)

#Dynamic format build up method
def formatter(in_t):
    #Accept only tuple
    if type(in_t) == tuple:
        #State the length of the numbers
        form_string = f"the {len(in_t)} numbers are: "
        #Perform action for every number in tuple
        for num in in_t:
            #add in format to base string
            form_string += "{:d}, "
        #return completed string after removing the last ', '
        return form_string.format(*in_t)[:-2]
    #Request new tuple
    else:
        print("Please verify your tuple.")

#Verify result
print(formatter(t3))

#Task Four
#Given tuple
t4 = (4, 30, 2017, 2, 27)

#Rearragned, position specified by index
#Option 1
Rearragned = "{:02d} " * len(t4)
print(Rearragned.format(t4[3],t4[4], t4[2], t4[0], t4[1]))

#Optoin 2
print(f"{t4[3]:02d} {t4[4]:d} {t4[2]:02d} {t4[0]:02d} {t4[1]:d}")

#Question: Which option is better?

#Task Five
list5 = ["oranges", 1.3, "lemons", 1.1]

#First print statement
print(f"The weight of an {list5[0][:-1]} is {list5[1]:.1f} and the weight of a {list5[2][:-1]} is {list5[3]:.1f}")

#Modified with 1.2 times weight and capitalized name
print(f"The weight of an {list5[0].upper()[:-1]} is {1.2 * list5[1]:.1f} and the weight of a {list5[2].upper()[:-1]} is {1.2 * list5[3]:.1f}")

#Task Six

#Write a table
fluff = [["Hammy", 9, "$35"], ["Teeny", 8, "$12"], ["Teeny2", 8, "$12"], ["Tiny", 8, "$15"], ["Jumbo", 6, "$75"], ["Jumbo Junior", 3, "$45"]]
for cute in fluff:
    print("{:^12}{:^3}{:^3}".format(*cute))

#Write a column
t6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#Bonus
print(("{:>5}"*len(t6)).format(*t6))