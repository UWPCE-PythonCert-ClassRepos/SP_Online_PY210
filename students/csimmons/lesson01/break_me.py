# Exploring Errors and Exceptions

# NameError - Note mispelling of variable "new_value" triggers the exception

# value = "Hello World"
# new_value = value + ', Python is better than Perl.'
# print(new_valew)

# TypeError - Note the attempt to concatenate a string and int triggers exception

# age = 21
# message = "I just turned " + age
# print(message)

# SyntaxError - Note missing colon after for loop (should be after 'colors' in line 18)
# triggers exception 

# colors = ['red', 'blue', 'green']
# for color in colors
#    print(color)

# AttributeError - Throws exception at line 24 because int type does not have an append() method. 
# value = 100
# new_value = value.append(100)
# print(new_value)