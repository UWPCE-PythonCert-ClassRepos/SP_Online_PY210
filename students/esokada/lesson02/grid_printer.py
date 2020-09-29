def samplegrid():
    divline = "+ - - - - + - - - - +"
    emptyline = "|         |         |"
    print(divline)
    print((emptyline + "\n") * 3, end = "")
    print(emptyline)
    print(divline)
    print((emptyline + "\n") * 3, end = "")
    print(emptyline)
    print(divline)

def print_grid(n):
    plus = "+ "
    minus = "- "
    bar = "|"
    emptyline = bar + " "*n + bar + " "*n + bar
    divline = plus + minus*(n // 2) + plus + minus*(n // 2) + plus
    print(divline)
    print((emptyline + "\n")*(n // 2), end = "")
    print(divline)
    print((emptyline + "\n")*(n // 2), end = "")
    print(divline)

def print_grid2(rc, u):
    plus = "+ "
    minus = "- "
    bar = "| "
    divseg = plus + minus*u
    divline = divseg*rc + plus + "\n"
    emptyseg = bar + " "*2*u
    emptyline = emptyseg*rc + bar + "\n"
    gridrow = divline + emptyline*u
    print(gridrow*rc + divline)


print_grid2(3, 4)