import os
os.system('cls')

def print_grid(box_count,box_size):
    

    dash_count = (box_size) 
    pipe_range = (box_size)
    

    plus = "+"
    minus = "-"
    space = " "
    pipe = "|"
    
    #Make the top line
    print(f'{plus}',end='')
    print (f'{(space+minus)*dash_count}{space}{plus}'*box_count)

    for box in range(box_count):
        for x in range(pipe_range):
            #Make all the middle lines
            print(f'{pipe}',end='')
            print (f'{space*box_size*2}{space}{pipe}'*box_count)
            
        #Make the bottom line
        print(f'{plus}',end='')
        print (f'{(space+minus)*dash_count}{space}{plus}'*box_count)

if __name__ == "__main__":
    print_grid(5,3)    
     

