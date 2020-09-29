# Part 1 make grid
# too many lines but solves the problem
line1="+ - - - - + - - - - +"
line2="|         |         |"
print(line1)
print(line2)
print(line2)
print(line2)
print(line2)
print(line1)
print(line2)
print(line2)
print(line2)
print(line2)
print(line1)

# simplier way, but not super simplified
line1='+ - - - - + - - - - +'
line2='|         |         |'
line2n='\n'.join([line1,line2,line2,line2,line2]*2)
print(line2n)
print(line1)


# Part 2 one variable grid
# this will look weird if the grid is even, please enter an odd number :)
hlist=[]
vlist=[]

# horizontals
def grid(n):
    for i in range(0, n):
        if i==0:
            hlist.append('+')
        elif i%2==0:
            hlist.append('-')
        else:
            hlist.append(' ')
    print((''.join(hlist)),'+')

#verticals
    for i in range(0, n):
        if i==0:
            vlist.append('|')
        else:
            vlist.append(' ')

    for i in range(n):
        print(''.join(vlist), '|')

#horizontals
    print((''.join(hlist)),'+')

grid(5)


#Part 3 two variable grid
hlist=[]

def super_grid(y, z):
    bar = ('|'+(' ' * z))*z +'|'

# horizontal boxes
    for i in range(0, z+1):
        if i==0:
            hlist.append('+')
        elif i%2==0:
            hlist.append('-')
        else:
            hlist.append(' ')
    print(''.join(hlist*z)+'+')

#vertical boxes
    for j in range(y):
        print(bar)
        for k in range(y):
            print(bar)
        print(''.join(hlist*z)+'+')

super_grid(3,5)


