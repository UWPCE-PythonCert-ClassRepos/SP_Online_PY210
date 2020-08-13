def print_grid(n):
    cellSize = n//2
    PrintLine(cellSize)
    for i in range(2):
        PrintCell(cellSize)
        PrintLine(cellSize)
    return True
    
def PrintLine(width):
    print('+','-'*width,'+','-'*width,'+')
    return True

def PrintCell(size):
    for i in range(size):
        print('|',' '*size,'|',' '*size,'|')
        
print_grid(21)