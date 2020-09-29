#case1: with the first and last items exchanged.
#case2: with every other item removed.
#case3: with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
#case4: with the elements reversed (just with slicing).
#case5: with the last third, then first third, then the middle third in the new order.

#TEST CASES
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
b_tuple = (2, 54, 13, 12, 5, 32, 9, 8, 7, 6, 3, 1, 99)

#CASE 1
def case1(x):
    if type(x) is tuple:
        y = list(x)
        first = y[0]
        last= y[-1]
        y[0]=last
        y[-1]=first
        return(tuple(y))
    else:
        return("{2}{1}{0}".format(x[0], x[1:len(x)-1], x[-1]))
    
assert case1(a_string)== "ghis is a strint"
assert case1(a_tuple)== (32, 54, 13, 12, 5, 2)

#CASE 2
def case2(x):
    if type(x) is tuple:
        y = list(x)
        y[::2]    
        return(tuple(y[::2]))
    else:
        return(x[::2])

assert case2(a_string) == "ti sasrn"
assert case2(a_tuple) == (2, 13, 5)

#CASE 3
def case3(x):
    return(x[4:-4:2])

assert case3(a_string) == ' sas'
assert case3(a_tuple) == ()
assert case3(b_tuple) == (5, 9, 7)

#CASE 4
def case4(x):
    return(x[::-1])

assert case4(a_tuple) == (32, 5, 12, 13, 54, 2)
assert case4(a_string) == 'gnirts a si siht'

#CASE 5
#case5: with the last third, then first third, then the middle third in the new order.

def case5(x):
    y = list(x)
    amt = int(round(len(y)/3))
    first = x[:-amt]#all but last 3rd (first 3rd+middle third)
    last = x[-amt:]#(approximately or exactly last 3rd)
    return last+first

assert case5(a_string) == 'tringthis is a s'
assert case5(a_tuple) == (5, 32, 2, 54, 13, 12)
assert case5(b_tuple) == (6, 3, 1, 99, 2, 54, 13, 12, 5, 32, 9, 8, 7)