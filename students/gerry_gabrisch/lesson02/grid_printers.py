#Lesson 2
#Gerry Gabrisch
#GridPrint1():
    #mainline = '+ - - - - + - - - - +'
    #regularline = '|         |         |\n'
    #print(mainline)
    #print(regularline * 4, end='')
    #print(mainline)
    #print(regularline * 4, end='')
    #print(mainline)
    
#GridPrint1()

#def print_grid(n):
    ##Where n is an odd number.
    ##segment is those number of places that are not plus signs.
    #segment = int(((n-1)/2))
    #mainLine = '+' + ' -' * segment + ' +'+ ' -' * segment + ' +'
    #secondLine = '|' + '  '* segment + ' |'+ '  '* segment+ ' |'
    #print(mainLine)
    #for i in range(segment):
        #print(secondLine)
    #print(mainLine)
    #for i in range(segment):
        #print(secondLine)  
    #print(mainLine)
#print_grid(5)

#def print_grid2(rows, cols):
    #mainLine = '+' + ' - - - - '
    #secondLine = '|' + '         '
    #for i in range(rows):
        #print(mainLine * cols +'+')
        #counter = 1
        #while counter <= 4:
            #counter +=1
            #print(secondLine * cols + '|') 
    #print(mainLine * cols +'+')
#print_grid2(10,1)

def print_grid_with_rounding(cells, cellsize):
    mainLine = '+' + ' - ' * cellsize
    secondLine = '|' + '   '* cellsize
    for i in range(cells):
        print(mainLine * cells +'+')
        counter = 1
        while counter <= cellsize:
            counter +=1
            print(secondLine * cells + '|') 
    print(mainLine * cells +'+')
print_grid_with_rounding(1,1)
