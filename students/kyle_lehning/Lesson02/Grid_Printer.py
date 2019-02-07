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
    multiplier = int(n/2) #forces an integer, rounds down if odd
    dash_line = '- ' * multiplier
    plus_line = '+ ' + dash_line + '+ ' + dash_line + '+'
    spaces = '  ' * multiplier
    print(plus_line)
    for x in range(2):
        for i in range(multiplier):
            print('| ' + spaces + '+ ' + spaces + '|')
        print(plus_line)
        
print_grid(15)    