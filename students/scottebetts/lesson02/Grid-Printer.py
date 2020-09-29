def print_grid(n):
    plus = '+'
    minus = '-'
    wall = '|'
    space = ' '
    cell = ( wall + space * n + wall + space * n + wall)
    vertice = (plus + space + (minus + space) * (n // 2) + plus + space + (minus + space) * (n // 2) + plus)
    print(vertice)
    for i in range(n // 2):
        print(cell)
    print(vertice)
    for i in range(n // 2):
        print(cell)
    print(vertice)

#print_grid(15)

def print_grid2(table_hw, cell_hw):
    plus = '+'
    minus = '-'
    wall = '|'
    space = ' '
    cell = (wall + ((space * cell_hw) * 2 + space + wall) * table_hw)
    vertice = ((plus + space + ((minus + space) * cell_hw) ) * table_hw + plus)

    for t in range(table_hw):
        print(vertice)
        for i in range(cell_hw):
            print(cell)
    print(vertice)

print_grid2(5,3)
#print_grid2(6,7)

