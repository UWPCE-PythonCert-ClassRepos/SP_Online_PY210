##Part1
##Print grid w/ out functions
##+ - - - - + - - - - +
##|         |         |
##|         |         |
##|         |         |
##|         |         |
##+ - - - - + - - - - +
##|         |         |
##|         |         |
##|         |         |
##|         |         |
##+ - - - - + - - - - +

##BEHOLD! my code:
print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '  ' * 4 + '+ ' + '  ' * 4 + '+')
print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+')


##Part2
##Build a generalized function to do be larger and smaller based on input number.
##eg.fun(3)
##+ - + - +
##|   |   |
##+ - + - +
##|   |   |
##+ - + - +

def print_grid(n):
    dash = "- " * int(floor(n / 2)) #need 1/2 the range of n on each side.  floor number to have extra space and to make int
    space = "  " * int(floor(n / 2)) #see above
    edge = "+ {dash}+ {dash}+".format(dash = dash) #build out the string to use
    mid = "| {space}| {space}|".format(space = space) #see above
    
    for i in range(n + 2): #add 2 b/c it starts at 0 and goes up to end number insead of through.
        if i == ceil(n/2) or i == 0 or i == n + 1: #if half way there, starting or ending
            print(edge) #WE'RE LIVING ON THE EDGE
        else:
            print(mid) #otherwise print the middle part
    return
    
print_grid(3)
print_grid(15)

##Part2
##Build a more genalized function that takes number of rows and columns with each having a given size
##eg.print_grid2(3,4)
#+ - - - - + - - - - + - - - - +
#|         |         |         |
#|         |         |         |
#|         |         |         |
#|         |         |         |
#+ - - - - + - - - - + - - - - +
#|         |         |         |
#|         |         |         |
#|         |         |         |
#|         |         |         |
#+ - - - - + - - - - + - - - - +
#|         |         |         |
#|         |         |         |
#|         |         |         |
#|         |         |         |
#+ - - - - + - - - - + - - - - +


#first number is number of rows and columns, 2nd is size of box.

def print_grid2(n, m):
    dash = "- " * m #set up the m number of dashes for the 'edge' pieces
    space = "  " * m #do the same for middle
    edge = "+" + (" {dash}+".format(dash = dash)) * n # repeate the edge sequence n times
    mid = "|" + (" {space}|".format(space = space)) * n #same for middle

    for i in range(n): # need to have n+1  edge pieces, go through n times and print the last one seperatly
        print(edge)
        for i in range(m): #print out the middle m times for n number of edges
            print(mid)
    print(edge) #print the closing edge
    return

print_grid2(3, 4)
print_grid2(5, 3)
