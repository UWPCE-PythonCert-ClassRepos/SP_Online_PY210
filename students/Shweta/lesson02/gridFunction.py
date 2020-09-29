#Print Grid Value using python function


def plusminus(m):
        for i in range(2):
            print('+',end=' ')
            print(('-' + ' ' ) * int(m),end=' ')
        print('+')
        
def pipe(m):
        for i in range(m):
            for i in range(3):
                print('|',end=' ')
                print('  ' * int(m),end=' ')
            print()
        


def print_grid(n):
    if n%2==0:
        print("Please enter odd number to make the grid")
    else:
        m=(n-1)//2
        plusminus(m)
        for i in range(2):
                 pipe(m)
                 plusminus(m)

print_grid(15)
