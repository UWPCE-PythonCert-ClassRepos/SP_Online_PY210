#Print Grid Value using python function with two arguments


def plusminus(n,m):
        for i in range(n):
            print('+',end=' ')
            print(('-' + ' ' ) * int(m),end=' ')
        print('+')
        
def pipe(n,m):
        for i in range(m):
            for i in range(n+1):
                print('|',end=' ')
                print('  ' * int(m),end=' ')
            print()
        


def print_grid(n,m):
    plusminus(n,m)
    for i in range(n):
        pipe(n,m)
        plusminus(n,m)

print_grid(5,3)
