def DefaultGridPrint():
    for i in range(11):
        if i == 0 or i == 5 or i == 10: 
            for j in range(11):
                if(j == 0 or j == 5 or j == 10):
                    print('+', end=' ')
                    if(j==10):
                         print('\n')
                else:
                    print('-', end=' ')
        else: 
            for k in range(11):
                if(k == 0 or k == 5 or k == 10):
                    print('|', end=' ')
                    if (k==10):
                        print('\n')
                else:
                    print(' ', end=' ')

def GridPrint_Square(n):
    n = n + 2
    midway = round(n/2)
    for i in range(n):
        if (i == 0 or i == midway or i == (n-1)): 
            for j in range(n):
                if(j == 0 or j == midway or j == (n-1)):
                    print('+', end=' ')
                    if(j==(n-1)):
                         print('\n')
                else:
                    print('-', end=' ')
        else: 
            for k in range(n):
                if(k == 0 or k == midway or k == (n-1)):
                    print('|', end=' ')
                    if (k==(n-1)):
                        print('\n')
                else:
                    print(' ', end=' ')

def GridPrint(n, s):
    n = (n*s) + n + 1
    for i in range(n):
        if (i == 0 or (i % (s+1) == 0)): 
            for j in range(n):
                if(j == 0 or  (j % (s+1) == 0)):
                    print('+', end=' ')
                    if(j==(n-1)):
                         print('\n')
                else:
                    print('-', end=' ')
        else: 
            for k in range(n):
                if(k == 0 or (k % (s+1) == 0)):
                    print('|', end=' ')
                    if (k==(n-1)):
                        print('\n')
                else:
                    print(' ', end=' ')
        
        
if __name__ == "__main__":
    DefaultGridPrint()
    GridPrint_Square(7)
    GridPrint(3,5)