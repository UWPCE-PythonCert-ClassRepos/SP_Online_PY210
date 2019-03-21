#This Prints the grid for Part 1 of Lesson 2
#This code prints a grid in a simple, hard-coded manner.

#Give names to symbols for clarity, assemble small sequences
dash = "- "
plus = "+"
bar = "|"
spaces = 9*" "

#Create the two types of rows, +- rows and bar (| and spaces) rows
horizontal_row = plus + " " + 4*dash + plus + " " + 4*dash + plus
bar_row = bar + spaces + bar + spaces + bar

#Prints grid in the format required
print(horizontal_row)
for x in range(0,4):
    print(bar_row)
print(horizontal_row)
for x in range(0,4):
    print(bar_row)
print(horizontal_row)