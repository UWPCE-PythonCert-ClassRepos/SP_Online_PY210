# ---------------------------------------------------------------------------- #
# Title: Fizz_Buzz.py
# Description: Prints the numbers 1 to 100:
#   for multiples of three print “Fizz” instead of the number
#   for the multiples of five print “Buzz” instead of the number
#   for numbers which are multiples of both three and five print “FizzBuzz”
#
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #
CountUp = 0
# ---------------------------------------------------------------------------- #

#Step 1 Display Welcome Message to the User
print()
print("Welcome, This script will count from 1 to 100 and display the following:\n\n"
      "Any values divisible by '3', will be replaced with the name 'Fizz'\n"
      "Any values divisible by '5', will be replaced with the name 'Buzz'\n"
      "Any values divisible by '3 & 5', will be replaced with the name 'FizzBuzz'\n")

input("Press Enter to Continue") # A pause for the user to read the welcome text
# Step 2 Use a "for" loop to iterate over the numbers and look for division matches as shown below
print("\nStarting to Count: from 1 to 100!\n")

# Using a range to run over numbers 1 - 100, the loop counts up by 1 with each iteration
for value in range(1,101):
    CountUp = CountUp + 1

# Display to user - only if the number is divisible by 3 then remove numbers that are divisible by 3 & 5,
    # if true replace number with "Fizz"
    if CountUp % 3 == 0 and CountUp % 5 != 0:
        print("Fizz")

# Display to user - only if the number is divisible by 5 then remove numbers that are divisible by 3 & 5,
    # if true replace number with "Buzz"
    elif CountUp % 5 == 0 and CountUp % 3 != 0:
        print("Buzz")

# Display to user - only if the number is divisible by both 3 & 5 then
    # if true replace number with "FizzBuzz"
    elif CountUp % 3 == 0 and CountUp % 5 == 0:
        print("FizzBuzz")

# Display to user - only if the number is NOT divisible by either 3 or 5 then, if true print only the raw number
    elif CountUp % 3 != 0 and CountUp % 5 != 0:
        print(CountUp)

print("\nCompleted processing the numbers to 100!!")



