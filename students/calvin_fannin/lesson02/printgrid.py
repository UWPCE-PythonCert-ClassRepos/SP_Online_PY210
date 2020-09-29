

def draw_grid():

    plus = '+'
    minus = ' -'
    blank = ' '
    pipe = '|'


    line = plus + minus * 4 + blank
    fill = pipe + blank + blank * 8

    print (line + line + plus)
    print (fill * 2 + pipe)
    print (fill * 2 + pipe)
    print (fill * 2 + pipe)
    print (line + line + plus)
    print (fill * 2 + pipe)
    print (fill * 2 + pipe)
    print (fill * 2 + pipe)
    print (line + line + plus)


def draw_grid2(grid_size):

    plus = '+'
    minus = ' -'
    blank = ' '
    pipe = '|'
    grid_size = round(abs(grid_size))
    #reate string for fill and line based on grind size
    line = plus + minus * (4 * grid_size ) + blank
    fill = pipe + blank + blank * (8 * grid_size)
    #print top line
    print (line + line + plus )
    #print box expanded by grid size
    print ((fill * 2 + pipe + "\n") * 4 * grid_size, end="")
    print (line + line + plus)
    print ((fill * 2 + pipe + "\n") *4 * grid_size, end="")
    print (line + line + plus)

def draw_grid3(rows_col=1,grid_size=1):

    plus = '+'
    minus = ' -'
    blank = ' '
    pipe = '|'

    rows_col = round(abs(rows_col))
    grid_size = round(abs(grid_size))
    #Create string for line
    line = plus + minus * (4 * grid_size ) + blank
    #create string for filler for box
    fill = pipe + blank + blank * (8 * grid_size)
    #Loop and create columns and rows specified in rows_col
    for row in range(rows_col):
        print ((line * rows_col) + plus )
        print ((fill * rows_col + pipe + "\n") * 4 * grid_size, end="")
    print (line * rows_col + plus)


draw_grid()
draw_grid2(3)
draw_grid3(3.4432,3)









