#part 1 draws a grid of a specified size
def grid():
    horz_border = ('+' + ' ' + ('- ' * 4)) * 2 + ('+')
    vert_border = ('|' + ' ' + (' ' * 8)) * 2 + ('|')
    size = 4
    
    print(horz_border)
    
    for i in range(size):
        print(vert_border) 
        
    print(horz_border)
    
    for i in range(size):
        print(vert_border) 
        
    print(horz_border)
    

#part 2 draws a grid of a variable size
def print_grid(n):
    horz_border = ('+' + ' ' + ('- ' * (n // 2))) * 2 + ('+')
    vert_border = ('|' + ' ' + (' ' * ((n // 2) * 2))) * 2 + ('|')
    grid_size = 1
    
    print(horz_border)
    
    while grid_size <= n:
        if n % 2 != 0:
            if grid_size == (n // 2) +1:
                print(horz_border)
            else:
                print(vert_border)
        else:
            print(vert_border)
            
            if grid_size == (n // 2):
                print(horz_border)
                
        grid_size += 1
        
    print(horz_border)

#part 3 draws a grid of varying rows/columns made up of cells of varying sizes
def print_grid2(a, b):
    horz_border = ('+' + ' ' + ('- ' * b)) * a + ('+')
    vert_border = ('|' + ' ' + (' ' * (b * 2))) * a + ('|')
    grid_size = 1
    rows_of_cells = 1
    
    print(horz_border)
    
    for x in range(a):
        while grid_size <= b:
            print(vert_border)
            
            grid_size += 1
        
        print(horz_border)
        
        grid_size -= b
        rows_of_cells += 1
    