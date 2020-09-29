# This program prints grid 
# First parameter controls the number of rows and columns
# Second parameter controls the size of the grid

def print_grid2(a, b):
    numSides = b
    rows = a
    plus = "+ "
    minus = "- "
    empty = "  "
    pipe = "| "
    NextLine = "\n"
    HoriLine = (plus + minus * numSides) * a + plus + NextLine
    VertLine = ((pipe + empty * numSides) * a + pipe + NextLine) * numSides
    print((HoriLine + VertLine) * a + HoriLine)
