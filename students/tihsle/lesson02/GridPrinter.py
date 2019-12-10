def GridPrinter1():

    # define printer characters
    plus = '+'
    minus = ' -'
    blank = ' '
    bar = '|'

    # construct grid components
    edge = plus + minus * 4 + plus + minus * 4 + plus
    row = bar + blank * 8 + bar + blank * 8 + bar

    #print grid
    print (edge)
    print (row)
    print (row)
    print (row)
    print (row)
    print (edge)
    print (row)
    print (row)
    print (row)
    print (row)
    print (edge)

def GridPrinter2(nsize):

    # define printer characters
    plus = '+'
    minus = ' -'
    blank = ' '
    bar = '|'

    # construct grid components
    edge = plus + minus * round(nsize/3 + 1) + plus + minus * round(nsize/3  + 1) + plus
    row = bar + blank * round(nsize/3 + 1) * 2 + bar + blank * round(nsize/3 +1)*2 + bar
    rows = round(nsize/3 + 1)

    #print grid
    print (edge)
    for line in range(rows):
        print (row)
    print (edge)
    for line in range(rows):
        print (row)
    print (edge)

def GridPrinter3(ncell,nsize):

    # define printer characters
    plus = '+'
    minus = ' -'
    blank = ' '
    bar = '|'

    # construct grid components
    edge = plus + (minus * round(nsize) + plus) * ncell
    row = bar + (blank * round(nsize*2) + bar) * ncell
    rows = round(nsize)
    cells = round(ncell)

    #print grid
    print (edge)
    for block in range(cells):
        for line in range(rows):
            print (row)
        print (edge)

GridPrinter1()
GridPrinter2(9)
GridPrinter3(3,4)
