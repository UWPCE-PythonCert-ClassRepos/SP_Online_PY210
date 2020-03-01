                    
def PrintGrid(iNumBlocks, iRowCols):
    x = iNumBlocks * iRowCols + (iNumBlocks+1)
    for j in range(x):
        if j == 0 or j%(iRowCols+1)==0:
            for i in range(x):
                if i == x -1:
                    print ('+')
                elif i == 0 or i%(iRowCols+1)==0:
                    print ('+', end = ' ')
                else:
                    print ('-', end = ' ')
        else:
            for i in range(x):
                if i == x -1:
                    print('|')
                elif i == 0 or i%(iRowCols+1)==0:
                    print ('|', end = ' ')
                else:
                    print(' ', end = ' ')




######
# main
                    
numBlocks = 2
numRowCols = 4
print("number of blocks is " + str(int(numBlocks)) + "x" + str(int(numBlocks)) + ", row col block size is " + str(int(numRowCols)))
PrintGrid(numBlocks,numRowCols)
