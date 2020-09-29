def print_grid(a):
    horz = '+' + a * ' -' + ' +' + a * ' -' + ' +'
    vert = '| ' + 2*a * ' ' + '|' + 2*a * ' ' + ' |'
    b=0
    print(horz)
    while b < a:
        print(vert)
        b += 1
    print(horz)
    b=0
    while b < a:
        print(vert)
        b += 1
    print(horz)
    
print_grid(0)
print_grid(1)
print_grid(2)

