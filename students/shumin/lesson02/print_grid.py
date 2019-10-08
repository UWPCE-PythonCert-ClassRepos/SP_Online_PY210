# This program prints grid
# The size of the grid is controlled by the parameter

def print_grid(n):
    numSides = n // 2
    plus = "+ "
    minus = "- "
    empty = "  "
    pipe = "| "
    NextLine = "\n"
    HoriLine = plus + minus * numSides + plus + minus * numSides + plus + NextLine
    VertLine = (pipe + empty * numSides + pipe + empty * numSides + pipe + NextLine) * numSides
    print(HoriLine + VertLine + HoriLine + VertLine + HoriLine)
