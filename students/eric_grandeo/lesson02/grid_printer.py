#Grid Printer

'''
for i in range(11):
    if i == 0 or i == 5 or i == 10:
        print('+' + ('-' * 4) + '+' + ('-' * 4) + '+')
    else:
        print("|" + '    ' + "|" + '    ' + '|')
'''

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

