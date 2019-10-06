# lesson 2.2: grid printer exercise, J. Umetsu

# part 1-2: print a 2x2 grid of variable-sized cells 
def print_grid(size):
    n = int(size/2)
    vertex='+'
    h_edge='-'
    v_edge='|'
    space = ' '
    
    # define text row for grid edges
    bound_row = vertex + space+ n*(h_edge+space) + vertex + space + n*(h_edge+space) + vertex

    # define text row for grid 
    spacing_row = v_edge + space + n*(space+space) + v_edge + space + n*(space+space) + v_edge    
    
    print(bound_row,end='')
    print(n*('\n'+spacing_row))
    print(bound_row,end='')
    print(n*('\n'+spacing_row))
    print(bound_row)


# part 3: print a grid given grid size (column,row) and cell size
def print_grid2(grid_size,cell_size):
    wall_start = '+ '
    wall_x = '- '
    cell_start = '| '
    cell_x = '  '

    wall = (cell_size*wall_x + wall_start)
    cell = (cell_size*cell_x + cell_start)
    
    wall_line = wall_start + wall*grid_size
    cell_line = cell_start + cell*grid_size
    
    def cell_row(size,cell_text,cell_wall):
        print(cell_text)
        if size == 1:
            print(cell_wall)
            return 1, cell_text, cell_wall
        return cell_row(size-1,cell_text,cell_wall)
    
    def print_cells(row_num,size,cell_text,cell_wall):
        cell_row(size,cell_text,cell_wall)
        if row_num==1:
            return 1,size,cell_text,cell_wall
        return print_cells(row_num-1,size,cell_text,cell_wall)
    
    print(wall_line)
    print_cells(grid_size,cell_size,cell_line,wall_line)
    
        
    
    