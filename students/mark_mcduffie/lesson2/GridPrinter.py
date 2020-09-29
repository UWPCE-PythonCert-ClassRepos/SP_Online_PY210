#Grid Printer part 2
#prints grid of any defined size
def print_grid(size):
    x = (size-1)/2
    x = int(x)
    y = (size-1)
    y = int(y)
    for i in range(y):
        if(i == 0 or i == (x) or i == y):
            plusLine(size)
            middleLine(size)
        else:
          middleLine(size)
    plusLine(size)
def plusLine(size):
     for i in range(2):
        print("+", end = ' ')
        n = size/2
        n = int(n)
        for i in range(n):
            print("-", end = ' ')
     print("+")

def middleLine(size):
    for i in range(2):
        print("|", end = ' '*size)
    print("|")

print_grid(15)

#GridPrinter part 3
#prints a grid of grids nested inside, taking twi parameters for
#the size of each grid
def print_grid2(x,y):
#x equals dimensions of the whole grid
#y equals dimensions of one cell
    for i in range(x):
        plusRow(x,y)
        body(x,y)
    plusRow(x,y)
def plusRow(x,y):
    for i in range(x):
        print("+" , end = ' ')
        for j in range(y):
            print("-", end = ' ')
    print("+")
def body(x,y):
    for i in range(y):
        for j in range(x):
            print("|  " , end = ' '* x)
        print("|")
print_grid2(5,3)
