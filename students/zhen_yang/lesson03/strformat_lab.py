##############################
# String Formatting Exercise #
##############################
# Task One #
old_tuple = (2,123.4567,10000,12345.67)
f_str ='file_{:03d} : {:10.2f}, {:.2e}, {:.3g}'.format(old_tuple[0],old_tuple[1],old_tuple[2],old_tuple[3]) 

print(f"Old_tuple: {old_tuple}")
print(f"1. Formated String: {f_str}")

############
# Task Two #
############
# Alternative ways to get the same result of task one
f_str =f"file_{old_tuple[0]:03d} : {old_tuple[1]:10.2f}, {old_tuple[2]:.2e}, {old_tuple[3]:.3g}"
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
    for i in range(1,num_count):
        form_string = form_string + ', {:d}'
    #print(f"The form string: {form_string} for tuple: {my_tuple}.")
    return form_string.format(*my_tuple)

# Calling the formatter()
my_numbers = (12, 55, 24000, 78) 
print(f" The {len(my_numbers)} numbers are: {formatter(my_numbers)}. ")




