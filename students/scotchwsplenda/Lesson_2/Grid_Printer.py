# Part 1

horGrid = 2*('+ ' + 4*'- ') + '+\n'
verGrid = 4*(2*('| ' + 4*'  ') + '|\n')
print(horGrid + verGrid + horGrid + verGrid + horGrid)

# Part 2

def print_grid(n):

    if n%2==0:
        size=n+1
    else:
        size=n

    midPt = n//2
    horGrid = 2*('+' + midPt*'- ') +'+'
    verGrid = 2*('|' + midPt*'  ') + '|'

    for i in range(size+1):
        if i==0 or i == midPt+1:
            print(horGrid)
        else:
            print(verGrid)
    print(horGrid)

a = input("What sized grid friend?  ")
print(print_grid(int(a)),str("wow thats a fancy grid!"))

# Part 3

def print_good_grid(a,b):

    horzgrid= a*('+' + b*'- ')+'+'
    vertgrid= a*('|'+ b*'  ')+'|'

    for i in range(a):
        print(horzgrid+(("\n"+vertgrid)*a))
    print(horzgrid)


z,x=input("please enter desired cell count, cell size  ").split(',')
print(print_good_grid(int(z),int(x)))
