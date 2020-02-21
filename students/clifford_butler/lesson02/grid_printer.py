# grid_printer exercise part 1 

def print_grid(n):
    for i in range(n):
        print(("+ " + "- " ) * (n - 1) + "+")
        
print_grid(15)