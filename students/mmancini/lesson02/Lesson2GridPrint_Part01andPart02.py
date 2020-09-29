
def PrintGrid(blkSize):
    for j in range(blkSize):
        if j == 0 or j == int(blkSize/2) or j == blkSize -1:
            for i in range(blkSize):
                if i == 0 or i == int(blkSize/2):
                    print ('+', end = ' ')
                elif i == blkSize - 1:
                    print ('+')
                else:
                    print ('-', end = ' ')
        else:
            for i in range(blkSize):
                if i == 0 or i == int(blkSize/2):
                    print ('|', end = ' ')
                elif i == blkSize - 1:
                    print ('|')
                else:
                    print (' ', end = ' ')


######
# main

numRowCols=6
print("row col block size is " + str(int(numRowCols/2)))
PrintGrid(numRowCols+3)
