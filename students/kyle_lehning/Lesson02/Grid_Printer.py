def print_grid_part1():
    plus_line = '+ - - - - + - - - - +'
    pipe_line = '|         |         |'
    print(plus_line)
    for i in range(4):
        print(pipe_line)
    print(plus_line)
    for i in range(4):
        print(pipe_line)
    print(plus_line)

def print_grid(n):
    multiplier = int(n/2) #Forces an integer, rounds down if odd
    dash_line = '- ' * multiplier
    plus_line = '+ ' + dash_line + '+ ' + dash_line + '+'
    spaces = '  ' * multiplier
    print(plus_line)
    for x in range(2): #Split by 2 because plus_line in the middle
        for i in range(multiplier):
            print('| ' + spaces + '+ ' + spaces + '|')
        print(plus_line)

def print_grid2(x,y):
    grid_size = int(x) #Forces an integer
    box_size = int(y) #Forces an integer
    dash_line = ' -' * box_size
    spaces = '  ' * box_size
    plus_line = '+'
    pipe_line = '|'
    for boxes in range(grid_size): #make the 2 line types based on grid size
        plus_line += dash_line + ' +'
        pipe_line += spaces + ' |' 
    print(plus_line) #First line
    for x in range(grid_size): #loop for each row of boxes
        for i in range(box_size): #loop to make box height
            print(pipe_line)
        print(plus_line)

print_grid2(5,3)    