# ------------------------------ #
# FizzBuzz Assignment for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/3/2019, Created and tested script
# ------------------------------ #

# ----- DATA ----- #
# ---------------- #


# ----- PROCESSING ----- #
# ---------------------- #


# ----- PRESENTATION ----- #
# ------------------------ #

i = 1
while i <= 100:
    if (i/3).is_integer() and (i/5).is_integer():  # If divisible by both 3 and 5...
        print("FizzBuzz")
    elif (i/3).is_integer():  # If divisible by 3...
        print("Fizz")
    elif (i/5).is_integer():  # If divisible by 5...
        print("Buzz")
    else:
        print(i)  # ...Print counter/number
    i += 1