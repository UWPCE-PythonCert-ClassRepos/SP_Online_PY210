def gridfunction():
    plus = "+"
    minus = "-"
    paren = "|"
    space = " "
    mid = paren + (" ")*9 + paren + (" ") * 9 + paren
    outline = plus + space + (minus + space) * 4 + plus + space + (minus + space) * 4 + plus
    print(outline)
    print(mid)
    print(mid)
    print(mid)
    print(mid)
    print(outline)
    print(mid)
    print(mid)
    print(mid)
    print(mid)
    print(outline)

def print_grid(n):
    outline = "+ " + ("- ") * (int(n/2)) + "+ " + ("- ")* (int(n/2)) + "+"
    mid = "|" + " "*n + "|" + " "*n + "|"
    print(outline)
    for i in range(int(n/2)):
        print(mid)
    print(outline)
    for i in range(int(n/2)):
        print(mid)
    print(outline)

def print_grid2(x,y):
    outline = ("+ " + ("- ") * y)*x +"+"
    middle = ("|" + (" ") * (y*2 + 1) ) * int(x) + "|"
    for j in range(x):
        print(outline)
        for i in range(int(y)):
            print(middle)
    print(outline)