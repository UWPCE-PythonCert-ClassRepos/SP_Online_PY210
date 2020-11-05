#-------------------------------------------#
#Tittle: Fizz_Buzz, PYTHON210
#Desc: Prints numbers 1 through 100 inclusive. Modifies returns if
#   multiple of 3, 5, or 3 and 5.
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Oct-25>, created file
#Brent Kieszling,<2020-Nov-1>, Updated syntax
#-------------------------------------------#

a = 1

# Loop through 'a' until it reaches 100
while a <= 100:

# Establish flags to track divisibility by 3 and 5.
    check_three = False
    check_five = False

# Check if divisible by 3 and a whole number
    if (a/3).is_integer():
        check_three = True

# Check if divisible by 5 and a whole number
    if (a/5).is_integer():
        check_five = True

# Display special message if 'a' is divisible by 3 or 5
    if check_three and check_five == True:
        print("FizzBuzz")
    elif check_three == True:
        print("Fizz")
    elif check_five == True:
        print("Buzz")
    else:
        print(a)

# Increment 'a'
    a += 1