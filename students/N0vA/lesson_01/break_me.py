# Write four functions that break with the most 
# common exceptions - NameError, TypeError, 
# SyntaxError, and AttributeError

# NameError
def simple_addition():
	x + 3

# TypeError
def simple_subtraction():
	x = 'food'
	x - 5

# SyntaxError
def a_function(name = 'Jim'):
	print(name)

# Attribute Error
def another_function(x):
	x.append(2)

