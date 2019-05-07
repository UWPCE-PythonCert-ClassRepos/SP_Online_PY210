# For part 2, create a function that will build a grid of a specific size

# Print a 2x2 grid of a specific size
# Here, n represents the number of symbols between the end points
# For example, n = 9 would draw the following grid
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
# If n is odd, there are (n-1)/2 dashes between the plus signs
# If n is even, there should be n/2 dashes between the plus signs

def print_grid(n):
    # Input parameter n is an integer related to the size of the grid
    # Define the four symbols used to print the grid
    plus = '+'
    dash = '-'
    pipe = '|'
    space = ' '
    # Form the two types of lines based on the input
    # Here, box_size is half of n (use integer division)
    box_size = n//2
    boundary_line = plus + dash*box_size + plus + dash*box_size + plus
    interior_line = pipe + space*box_size + pipe + space*box_size + pipe
    num_lines = (box_size * 2) + 3
    for line in range(num_lines):
        if line in {0,num_lines//2,num_lines-1}:
            print(boundary_line)
        else:
            print(interior_line)

if __name__ == "__main__":
    # Run some tests on different size grids
    n_test = [3,6,9,15,20]
    for n in n_test:
        print('\nPrinting grid of size %i\n' % n)
        print_grid(n)
