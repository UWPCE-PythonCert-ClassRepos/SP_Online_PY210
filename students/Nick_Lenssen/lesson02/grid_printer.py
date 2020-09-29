def make_grid(n):
    size = n +2
    for j in range(size):
        if j == 0 or j == int(size/2) or j == size -1:
            for i in range(size):
                if i == 0 or i == int(size/2):
                    print ('+', end = ' ')
                elif i == size - 1:
                    print ('+')
                else:
                    print ('-', end = ' ')
        else:
            for i in range(size):
                if i == 0 or i == int(size/2):
                    print ('|', end = ' ')
                elif i == size - 1:
                    print ('|')
                else:
                    print (' ', end = ' ')
def make_grid2(rows_cols, n):
    size = rows_cols * n + (rows_cols+1)
    for j in range(size):
        if j == 0 or j%(n+1)==0:
            for i in range(size):
                if i == size -1:
                    print ('+')
                elif i == 0 or i%(n+1)==0:
                    print ('+', end = ' ')
                else:
                    print ('-', end = ' ')
        else:
            for i in range(size):
                if i == size -1:
                    print('|')
                elif i == 0 or i%(n+1)==0:
                    print ('|', end = ' ')
                else:
                    print(' ', end = ' ')


                    

make_grid(9)
make_grid2(3,4)
