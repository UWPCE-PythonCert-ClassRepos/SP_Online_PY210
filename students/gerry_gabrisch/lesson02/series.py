def fibonacci(n):
    '''returns the nth number of the Fibonacci
    sequence.  where the first position is indexed at 0.
    n must be an iteger greater than or equal to 0'''
    #these are the first two numbers in the sequence.
    fib = [0,1]
    #If the users enters a number less than 2 then just get that number from the list.
    if n <= 1:
        #return list item at n
        return fib[n]
    else:
        #The first two position are already defined so only calculate to the sequence n-1 times to get that position.
        for i in range(n-1):
            #get the two list items and add them together...
            nextnum = fib[0] + fib[1]
            #shift all the numbers in the list one position to the left.
            fib = [fib[1], nextnum]
        #The last number in the list is the postion the user asked for so return it.    
        return fib[1]
    
def lucas(n):
    '''returns the nth number of the Lucas
    sequence.  where the first position is indexed at 0
    n must be an iteger greater than or equal to 0'''
    #these are the first two numbers in the Lucas sequence.
    luke = [2,1]
    #If the users enters a number less that 2 then just get that number from the list.
    if n <= 1:
        #return list item at n
        return luke[n]
    else:
        #The first two position are already defined so only calculate to the sequence n-1 times to get that position.
        for i in range(n-1):
            #get the two list items and add them together...
            nextnum = luke[0] + luke[1]
            #shift all the numbers in the list one position to the left.
            luke = [luke[1], nextnum]
        #The last number in the list is the postion the user asked for so return it.    
        return luke[1]
    


def sum_series(n, x = 0, y = 1):

        '''sum_series returns the nth number of the Fibonacci, the Lucas sequence
        or the Foo sequence where the first position is indexed at 0.  Arguments x and y as integers
        are optional.  
        Argument n as an integer is required.  
        
        (n, 0, 1) returns the Fibinacci sequence at postion n.
        (n, 2, 1) returns the Lucas sequence at postion n
        (n, 3, 1)returns the Foo sequence at potions n.
        
        Any other combo (including no optional parameters) returns the Fibonacci sequence at postion n.'''
        
        ###Fibonacci sequence calculator....
        #these are the first two numbers in the sequence.
        fib = [0,1]
        #If the users enters a number less that 2 then just get that number from the list.
        if n <= 1:
            #return list item at n
            fibnum = fib[n]
        else:
            #The first two position are already defined so only calculate to the sequence n-1 times to get that position.
            for i in range(n-1):
                #get the two list items and add them together...
                nextnum = fib[0] + fib[1]
                #shift all the numbers in the list one position to the left.
                fib = [fib[1], nextnum]
            #The last number in the list is the postion the user asked for so return it.    
            fibnum = fib[1]    
        ###Lucas sequence calculator...
        #these are the first two numbers in the Lucas sequence.
        luke = [2,1]
        #If the users enters a number less that 2 then just get that number from the list.
        if n <= 1:
            #return list item at n
            lukenum = luke[n]
        else:
            #The first two position are already defined so only calculate to the sequence n-1 times to get that position.
            for i in range(n-1):
                #get the two list items and add them together...
                nextnum = luke[0] + luke[1]
                #shift all the numbers in the list one position to the left.
                luke = [luke[1], nextnum]
            #The last number in the list is the postion the user asked for so return it.    
            lukenum = luke[1]   
        
        ###Foo sequence
        #these are the first two numbers in the foo sequence.
        foo = [3,2]
        #If the users enters a number less that 2 then just get that number from the list.
        if n <= 1:
            #return list item at n
            foonum = foo[n]
        else:
            #The first two position are already defined so only calculate to the sequence n-1 times to get that position.
            for i in range(n-1):
                #get the two list items and add them together...
                nextnum = foo[0] + foo[1]
                #shift all the numbers in the list one position to the left.
                foo = [foo[1], nextnum]
            #The last number in the list is the postion the user asked for so return it.    
            foonum = foo[1]          
        
        if x == 0 and y == 1:
            return fibnum
        if x == 2  and y == 1:
            return lukenum
        if x==3 and y ==2:
            return foonum
        else:
            return fibnum