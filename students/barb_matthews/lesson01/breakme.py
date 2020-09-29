## simple throw exceptions program
## by: b. matthews 9/1/2020

value = 1

#nameError
def whoops1(value):
	print ("haha") 
#whoops1(val)
	
#TypeError
def whoops2(value):
	print ("oh no")
	value == len(42)

#print (whoops2(value))

#SyntaxError
#def functNo()
#print ("hi")

#AttributeError
def get_upper(my_string):
  return my_string.upper()

get_upper(42)



