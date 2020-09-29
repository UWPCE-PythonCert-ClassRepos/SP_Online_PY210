# break_me assignment

# NameError exception 
def my_name_error():
    my_nnme_error()


# TypeError exception
def my_type_error():
    num = '5' 
    num = num + 1

# SyntaxError exception
#def my_syntax_error():
#    num = num + (2 * 3

# AttributeError
def my_attribute_error(num):
    num.append(5)


# calling each function
#my_name_error()
#my_type_error()
#my_syntax_error()
my_attribute_error(5)

