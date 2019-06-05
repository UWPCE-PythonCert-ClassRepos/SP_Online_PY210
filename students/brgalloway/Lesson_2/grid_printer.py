# part 1
def grid_printer():
    row    = (' ' + '-' + ' ') * 2 
    column = '|' + '   ' * 2 + '|' + '   ' * 2 + '|'
    cross  = '+'
    print(cross + row + cross + row + cross)
    print(column)
    print(column)
    print(cross + row + cross + row + cross)
    print(column)
    print(column)       
    print(cross + row + cross + row + cross) 

grid_printer()

# part 2
def grid_printer_2(num):
    row    = (' ' + '-' + ' ') * num
    column = '|' + '   ' * num + '|' + '   ' * num + '|'
    cross  = '+'
    print(cross + row + cross + row + cross)
    for i in range(num):
        print(column)
    print(cross + row + cross + row + cross)
    for i in range(num):
        print(column)
    print(cross + row + cross + row + cross) 

grid_printer_2(3)

# part 3
def grid_printer_3(a, b):
    row    = (' ' + '-' + ' ') * b
    column = '|' + '   ' * b 
    cross  = '+'
    def make_row():
        for i in range(a):
            print(cross+ row, end='')
        print(cross)
    def make_col():
        for i in range(a + 1):
            print(column + '' * b, end='')
    for i in range(a):
        make_row()
        for j in range(b):
            make_col()
            print()
    make_row()

grid_printer_3(5,3)