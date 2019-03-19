# Author    :    Chieu Quach
# Assignment:    Lesson02
# Exercise  :    Fibonacci Series Exeise
# Detail    :    Computing Fibonacci and Lucas Series

def fibonacci(n):
      
        
        # Check value n. If value of n is 0 or 1 then return value n of 0
        # 1  and print value
        if n <=  1:
                return n
        else: 
        # if value n is greater than 1 then add two previous values and
        # return the sum of it
           
                return (fibonacci(n -1) + fibonacci(n-2))

       
def lucas(n):       
       
        # Scan value n. If value of n is 2 or 1 then prints output of
        # value. Otherwise, total two previous value and prints output. 
       
        if n == 0:
                n = 2
                return n
        elif n == 1:
                n = 1
                return n
        else:
        # If forloop value of n is greater than 1 than move 2nd argument value
                
                return (lucas(n - 1) + lucas(n - 2))
                        

        
def sum_series(n,n0=0,n1=1):
        e=0
        
        # Assert statement to check value n is 30. If not it would have asserterror.      
        assert n == 30, "n has to be 30"
       # assert n0 == 2, "n has to be 2"
       # assert n1 == 1,  "n has to be 1"
        # Loop to number of n
        for e in range(0,n):
                # if no optional condition is passed then call fibonacci function
                # otherwise call lucas function
               if not n0:
                        print (fibonacci(e))
                        # The following assert statements from fibonacci
                        # check if output values match
                        # with the values listed here. If they don't match
                        # then error asserterror message will generate.
                        assert fibonacci(0) == 0
                        assert fibonacci(1) == 1
                        assert fibonacci(2) == 1
                        assert fibonacci(3) == 2
                        assert fibonacci(4) == 3
                        assert fibonacci(5) == 5
                        assert fibonacci(6) == 8
                        assert fibonacci(7) == 13
               else:
                        # Assert statement to check value n0 is 2. If not it would have asserterror.
                        # Assert statement to check n is 1. If not it would have asserterror.
                        assert n0 == 2, "n has to be 2"
                        assert n1 == 1,  "n has to be 1"
                                                 
                        print (lucas(e))
                        # The following assert statements from lucas
                        # check if output values match
                        # with the values listed here. If they don't match
                        # then error asserterror message will generate.
                        assert lucas(0) == 2
                        assert lucas(1) == 1
                        assert lucas(2) == 3
                        assert lucas(3) == 4
                        assert lucas(4) == 7
                        assert lucas(5) == 11
                        assert lucas(6) == 18
                        assert lucas(7) == 29

# Main Function

# Calling Fibonacci 
sum_series(30)
print("\n")
# Calling Lucas
sum_series(30,2,1)



