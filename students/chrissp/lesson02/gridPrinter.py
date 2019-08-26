def simpleGrid():
    bar = '+' + (' -' * 4) + ' +' + (' -' * 4) + ' +' #this is the +--+ line
    line = '|' + (' ' * 8) + ' |' + (' ' * 8) + ' |' #this is the |   | line

    print(bar)
    for i in range(4):
        print(line)
    print(bar)
    for i in range(4):
        print(line)
    print(bar)
#simpleGrid()

def print_grid(s):
    split_size = int(s / 2) #divide the size given between two cols or rows
    bar = '+' + (' -' * split_size) + ' +' + (' -' * split_size) + ' +'
    line = '|' + (' ' * s) + '|' + (' ' * s) + '|'

    print(bar)
    for i in range(split_size):
        print(line)
    print(bar)
    for i in range(split_size):
        print(line)
    print(bar)
#print_grid(4)

def print_grid2(w, h):
    bar = ('+' + (' -' * h) + " ") * w + '+'
    line = ('|' + ('  ' * h) + " ") * w + '|'

    for lines in range(w):
        print(bar)
        for bars in range(h):
            print(line)
    print(bar)
#print_grid2(5, 3)