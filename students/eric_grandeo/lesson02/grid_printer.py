#Grid Printer

#first part of the exercise
'''
for i in range(11):
    if i == 0 or i == 5 or i == 10:
        print('+' + ('-' * 4) + '+' + ('-' * 4) + '+')
    else:
        print("|" + '    ' + "|" + '    ' + '|')
'''
'''
#function that takes one argument
def print_grid(n):
    for i in range(n+1):
        if i == 0 or i == (n+1)/2:
            print('+' + '-' * (n//2) + '+' + '-' * (n//2) + '+')
            
        else:
            print("|" + ' ' * (n//2) + "|" + ' ' * (n//2) + '|')
    print('+' + '-' * (n//2) + '+' + '-' * (n//2) + '+')
    

print_grid(3)
print_grid(9)
print_grid(15)
'''


#function that takes 2 arguments

def print_grid2(a,b):
    plus = '+'
    lines = (b * '-') + plus
    col = '|'
    rows = (b * ' ') + col

    #print(plus + lines * (a+1))
    #print(col + rows * (a+1))
    
    for i in range(a):
        print(plus + lines * (a)) 
        for i in range(b):
            print(col + rows * (a)) 
    print(plus + lines * (a)) 


print_grid2(3,4) 
print_grid2(5,3)
#print_grid2(5,1)


