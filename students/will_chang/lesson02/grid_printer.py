def explicit_grid():
    """Prints square grid whose size is independent of user input."""
    n = 8
    num_segments = n//2 # assume odd numbers will round down
    plus_minus_pattern = ('+ ' + ('- ' * num_segments) + '+ ' + ('- ' * num_segments) + '+')
    
    if n % 2 == 0: # if input is an even number
        vert_bar_pattern = ('|' + (' '*n) + ' |' + (' '*n)+ ' |')
    else:
        vert_bar_pattern = ('|' +(' '*n) + '|' + (' '*n) +  '|')
    
    print(plus_minus_pattern) # top segment
    
    for i in range(num_segments):
        print(vert_bar_pattern)
        
    print(plus_minus_pattern) # middle segment
    
    for i in range(num_segments):
        print(vert_bar_pattern)
        
    print(plus_minus_pattern) # bottom segment
    

def print_grid(n):
    """Prints grid based on user input n."""
    num_segments = n//2 # assume odd numbers will round down
    plus_minus_pattern = ('+ ' + ('- ' * num_segments) + '+ ' + ('- ' * num_segments) + '+')
    
    if n % 2 == 0: # if input is an even number
        vert_bar_pattern = ('|' + (' '*n) + ' |' + (' '*n)+ ' |')
    else:
        vert_bar_pattern = ('|' +(' '*n) + '|' + (' '*n) +  '|')
    
    print(plus_minus_pattern) # top segment
    
    for i in range(num_segments):
        print(vert_bar_pattern)
        
    print(plus_minus_pattern) # middle segment
    
    for i in range(num_segments):
        print(vert_bar_pattern)
        
    print(plus_minus_pattern) # bottom segment
    

def print_grid2(row_col, num_segments):
    """Prints grid based on user inputs of #rows/cols and #segments."""
    plus_minus_pattern = row_col * ('+ ' + ('- ' * num_segments)) + '+'
    num_space = (2 * num_segments) + 1
    vert_bar_pattern = row_col * ('|' + (' ' * num_space)) + '|'

    for i in range(row_col): # each iteration: plus_minus_pattern and (vert_bar_pattern X num_segments)
        print(plus_minus_pattern)
        for j in range(num_segments):
            print(vert_bar_pattern)
    print(plus_minus_pattern) # bottom segment
    
        
