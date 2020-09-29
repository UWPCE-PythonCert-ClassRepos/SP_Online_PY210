##############################
# String Formatting Exercise #
##############################
# Task One #
old_tuple = (2, 123.4567, 10000, 12345.67)
# *old_tuple is to uppack the tuple
f_str = 'file_{:03d} : {:10.2f}, {:.2e}, {:.3g}'.format(*old_tuple)

print(f"Old_tuple: {old_tuple}")
print(f"1. Formated String: {f_str}")

############
# Task Two #
############
# Alternative ways to get the same result of task one
f_str = f"file_{old_tuple[0]:03d} : {old_tuple[1]:10.2f}, \
{old_tuple[2]:.2e}, {old_tuple[3]:.3g}"
print(f"2. Formated String: {f_str}")


##############
# Task Three #
##############
# Rewrite "the 3 number are: {:d}, {:d}, {:d}".format(1,2,3) to
# take an arbitrary number of values.
# define formatter((tuple)) function
def formatter(my_tuple):
    form_string = "{:d}"
    # get the total number of values in my_tuple
    num_count = len(my_tuple)
    for i in range(1, num_count):
        form_string = form_string + ', {:d}'
    #print(f"The form string: {form_string} for tuple: {my_tuple}.")
    return form_string.format(*my_tuple)

# Calling the formatter()
my_numbers = (12, 55, 24000, 78)
print(f" The {len(my_numbers)} numbers are: {formatter(my_numbers)}. ")


#############
# Task Four #
#############
# Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
# using string formating to print
# 02 27 2017 04 30
my_tuple = (4, 30, 2017, 2, 27)
print(f"{my_tuple}")
print("{:02d} {:d} {:d} {:02d} {:02d}\
".format(my_tuple[3], my_tuple[4], my_tuple[2], my_tuple[0], my_tuple[1]))


#############
# Task Five #
#############
# Give an input list: ['oranges',1.3,'lemons',1.1]
# Display 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
# by using f-string
my_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {my_list[0]} is {my_list[1]} and the weight of a \
{my_list[2]} is {my_list[3]}.")

print(f"The weight of an {my_list[0].upper()} is {my_list[1]*1.2} \
and the weight of a {my_list[2].upper()} is {my_list[3]*1.2}.")


#############
# Task Six  #
#############
# print a table of several rows, each with a name, an age and a cost.
# Make sure some of the costs are in the hundreds and thousands to
# check your alignment specifiers.
my_row_1 = ['Alexadra', 28, 3.456]
my_row_2 = ['Bill', 46, 1078.02]
my_row_3 = ['Catherine', 39, 88.345]
my_row_4 = ['Peter', 8, 4876.175]
my_table = [my_row_1, my_row_2, my_row_3, my_row_4]
print(" Organized  Table ")
for i in my_table:
    print(f"{i[0]:<12} {i[1]:>2d} {i[2]:>8,.2f}")

# Create a tuple with 10 consecutive numbers
# print the tuple in columns that are 5 characters wide using one short line.
my_tuple = tuple(range(1, 11))
my_formater = '{:5d}' * 10
print(my_formater.format(*my_tuple))
