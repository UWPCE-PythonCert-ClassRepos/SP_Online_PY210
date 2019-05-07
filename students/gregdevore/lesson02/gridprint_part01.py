# For part 1, just print a simple grid
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Define the four different symbols
plus = '+'
dash = '-'
pipe = '|'
space = ' '

# Create the two types of lines using string concatenation
boundary_line = plus + dash*4 + plus + dash*4 + plus
interior_line = pipe + space*4 + pipe + space*4 + pipe

# 11 lines total
# The first, last, and middle are boundary lines
# The rest are interior lines
lines = 11
for line in range(lines):
    if line in {0,lines//2,lines-1}:
        print(boundary_line)
    else:
        print(interior_line)
