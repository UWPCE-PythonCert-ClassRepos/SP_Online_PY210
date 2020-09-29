
def print_grid_part1():
    """ Prints 2x2 grids of cells of 4 dashes sized."""
    
    plus_space = '+ '
    minus_space = '- '
    plus = '+'
    bar_space = '| '
    bar = '|'
    double_space = '  '
    
    """Prints one horizontal line and verical bars in the first row
    of cells then repeats it twice."""
    print(((plus_space + minus_space * 4) * 2 + plus + "\n" + ((bar_space 
            + double_space * 4) * 2 + bar + "\n") * 4) * 2, end="\b" )
            
    """Prints bottom horizontal line. """        
    print((plus_space + minus_space * 4) * 2 + plus)
    
   
def print_grid_part2(n):
    """ Prints 2x2 grids of a given sized cell."""
    
    cell_size = int((n-1)/2)
    
    plus_space = '+ '
    minus_space = '- '
    plus = '+'
    bar_space = '| '
    bar = '|'
    double_space = '  '
    
    """Prints one horizontal line and verical bars in the first row
    of cells then repeats it twice."""
    print(((plus_space + minus_space * cell_size) * 2 + plus + "\n"
            + ((bar_space + double_space * cell_size) * 2 + bar + "\n") 
            * cell_size) * 2 , end="\b")
            
    """Prints bottom horizontal line. """ 
    print((plus_space + minus_space *cell_size)*2 + plus)


def print_grid_part3(num_col_row,cell_size):
    """ Prints specified number of rows/columns of 
    a given sized cell"""
    
    plus_space = '+ '
    minus_space = '- '
    plus = '+'
    bar_space = '| '
    bar = '|'
    double_space = '  '
    
    """Prints one horizontal line and verical bars in the first row
    of cells then repeats it by the number of rows."""   
    print(((plus_space + minus_space * cell_size) * num_col_row + plus + "\n"
            +((bar_space + double_space * cell_size) * num_col_row + bar 
            + "\n") * cell_size) * num_col_row, end="\b")
            
    """Prints bottom horizontal line. """            
    print((plus_space + minus_space * cell_size) * num_col_row + plus)
    


print_grid_part1()
print_grid_part2(9)
print_grid_part3(6,1)