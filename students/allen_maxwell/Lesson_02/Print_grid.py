# Allen Maxwell
# Python 210
# 10/27/2019
# 
# Print_grid.py

# Part 1
horGrid = 2*('+ ' + 4*'- ') + '+\n'
verGrid = 4*(2*('| ' + 4*'  ') + '|\n')
print(horGrid + verGrid + horGrid + verGrid + horGrid)

# Part 2
def print_grid(n):
    if n%2 == 0:
        size = n+1
    else:
        size = n

    midPt = n//2
    horGrid = 2*('+ ' + midPt*'- ') +'+'
    verGrid = 2*('| ' + midPt*'  ') + '|'

    for i in range(size+1):
        if i == 0 or i == midPt+1:
            print(horGrid)
        else:
            print(verGrid)
    print(horGrid)

# Part 3
def print_grid2(a,b):
    horGrid = a*('+ ' + b*'- ') +'+'
    verGrid = a*('| ' + b*'  ') + '|'

    for i in range(a):
        for i in range(b+1):
            if i == 0:
                print(horGrid)
            else:
                print(verGrid)

    print(horGrid)