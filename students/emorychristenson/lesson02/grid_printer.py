def print_grid(x, y):
    for _ in range(x):
        print(("+ " + "- " * y) * x + "+")
        for _ in range(y):
            print(("| " + "  " * y) * x + "|")
    print(("+ " + "- " * y) * x + "+")
    
print_grid(6,7)
