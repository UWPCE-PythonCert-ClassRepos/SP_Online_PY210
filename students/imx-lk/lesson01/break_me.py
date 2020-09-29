

#I decided not to use try and except and or raise because w'ere trying to cause an exception to happen

#Not defining a variable
def name_error():
    a = int(input("Enter any number and I will add 5 to it "))
    c = a +b
    print("The answer is ", c)

#adding two different data types
def type_error():
    a = int(input("Enter any number and I will add 5 to it "))
    c = a + 'five'
    print("The answer is ", c)

#The colon at the end of defining my function syntax_error
def syntax_error()
    a = int(input("Enter any number and I will add 5 to it "))
    c = a + 5
    print("The answer is ", c)

#applying a string attribute to an int
def attribute_error():
    a = 5
    a.capitalize()
    print(a)

#calling my functions
name_error()
type_error()
syntax_error()
attribute_error()

