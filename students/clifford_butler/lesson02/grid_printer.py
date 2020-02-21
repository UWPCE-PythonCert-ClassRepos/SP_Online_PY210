# grid_printer exercise part 1 

def print_grid(n):
    for i in range(n):
        print(("+ " + "- " ) * (n - 1) + "+")
        
print_grid(15)

#################################################
# grid_printer exercise part 2

def print_grid(n):
    for i in range(n):
        print(("+ " + "- " ) * (n - 1) + "+")
        for j in range(n):
            print(("| " + "  ") * (n - 1) + "|") 
    print(("+ " + "- ") * (n - 1) + "+")    
        
print_grid(8)

#################################################
#grid_printer exercise part 3

def print_grid(x, y):
    for i in range(x):
        print(("+ " + "- " * y) * x + "+")
        for j in range(y):
            print(("| " + "  " * y) * x + "|")
    print(("+ " + "- " * y) * x + "+")


print_grid(3, 3)