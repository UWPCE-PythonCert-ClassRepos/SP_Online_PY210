LESSON 3

---slicing_lab.py---
Exercise to practice manipulating sequences with slicing as follows:
# Create functions to take a sequence and create a copy except:
# 1) with the first and last items exchanged
# 2) with every other term removed
# 3) with the first and last (4) terms removed
# 4) with reversed elements
# 5) with last 1/3, then first 1/3, then middle 1/3 in the new order

Validated using assert statements


---list_lab.py---
Exercise to practice manipulating lists as follows:
# 1)  Create a list containing "Apples", "Pears", "Oranges" and "Peaches"
#     - Display the list
#     - Ask the User for another fruit and add to the end of list
#     - Display the new list
#     - Ask the user for a number and display the number and corresponding fruit on a 1-is-first basis.
#     - Add another fruit to the beginning of the list using "+" and display
#     - Add another fruit to the beginning of the list using insert() and display the list
#     - Display all fruits that begin with 'P' in the list
#
# 2)  Using the list from Series 1 above
#     - Display the list
#     - Remove the last fruit from the list
#     - Display the new list
#     - Ask the user for a fruit to delete, find it, and delete it
#     - (Bonus) Multiply the list by 2, keep asking until a match is found,
#       then delete all occurrences.
#
# 3)  Using the list from Series 1 above
#     - Ask the user to input diplaying a line like, "Do you like apples?"
#       for each fruit on the list (making the fruit lowercase)
#     - For each "no" response, delete from the list.
#     - For any answer that is not "yes" or "no" prompt the user to answer "yes" or "no"
#     - Display the new list
#
# 4)  - Make a new list with the contents of the original but with all the letters in each item reversed.
#     - Delete the last item from the original list.
#     - Display the original list and the copy.



---strformat_lab.py---
Exercise to practice creating and manipulating formatted strings with the following tasks:
# Task 1
#    Write a format string to take the tuple (2, 123.4567, 1000, 1234.67)
#    and produce 'file_002 :  123.46, 1.00e+04, 1.23e+04'
#
# Task 2
#    Repeat Task 1 but this time use an alternate type of format string.
#    consider using f-strings.
#
# Task 3
#    Rewrite, "the 3 numbers are: {:d}, {:d}, {:d}",format(1,2,3) to take
#    arbitrary values - and an arbitrary number of values.  Allow it to be
#    a string called by either a literal or by a name.
#
# Task 4
#    Given a (5) element tuple (4, 30, 2017, 2, 27) use string formatting
#    to print '02 27 2017 04 30'
#
# Task 5
#    Given the list ['oranges', 1.3, 'lemons', 1.1]
#    write an f-string that will display, "The weight of an orange is 1.3 and
#    the weight of a lemon is 1.1"
#    Now see if you can change the names to uppercase and make the weight 20%
#    higher for each.
#
# Task 6
#   Write a python code to print a table of several rows, each with a name
#   and age, and a cost.  Make sure some of the costs are in the hudreds
#   and thousands to test your alignment.
#
#   And for an extra task, given a tuple with (10) consecutive numbers,
#   can you work how to quickly print the tuple in columns that are (5)
#   characters wide?  HINT: Make it a one-liner.



---Mailroom.py---
Part 1:
# Program takes a list of donations made by (6) donors, each donating up to 3x with varying amounts
# Program displays an intro message and asks user to select a task from the main menu
#
# If user selects option 1 by inputing "1" or anything containing "send" or "thank":
#   - User is asked for a name.  If name is a previous donor, a new donation record is made for them
#       - If name is a prior donor, program proceeds
#       - If name is not a prior donor, user is asked to confirm the new name, then program proceeds
#   - User is asked for a donation amount.  This amount is recorded on the new donation record
#   - A formatted email message is written thanking the donor for their donation
# User is returned to main menu
#
# If user selects option 2 by inputting "2" or anything containing "record" or "view", a report with the following is generated:
#   - Donor name (one listing/row per donor)
#   - Total net donation by that donor
#   - Number of donations made by that donor
#   - Average donation
# User is returned to main menu
#
# If user selects option 3 by inputing "3" or "quit" the program terminates.
#
# If at ANY prompt the user inputs "back" the function terminates and returns to main menu.
