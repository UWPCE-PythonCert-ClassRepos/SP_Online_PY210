# grid_printer exercise part 1 

def print_grid(n):
    for i in range(n):
        print(("+ " + "- " ) * (n - 1) + "+")
        
print_grid(15)

# grid_printer exercise part 2

def print_grid(n):
    for i in range(n):
        print(("+ " + "- " ) * (n - 1) + "+")
        for j in range(n):
            print(("| " + "  ") * (n - 1) + "|") 
    print(("+ " + "- ") * (n - 1) + "+")    
        
print_grid(8)