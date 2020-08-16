def PrintGrid(cells, size):
    PrintLine(cells, size)
    for i in range(cells):
        PrintCell(cells, size)
        PrintLine(cells, size)
    return True
    
def PrintLine(cells, width):
    for i in range(cells):
        print('+', '-'*width, end = ' ')
    print('+')
    return True

def PrintCell(cells, size):
    for i in range(size):
        for i in range(cells):
            print('|', ' '*size, end = ' ')
        print('|')
    return True

PrintGrid(10,1)