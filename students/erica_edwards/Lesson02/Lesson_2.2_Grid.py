import os
os.system('cls')

size = 9
if size %2 == 0:
    size = size + 1

dash_count = (size - 1)//2 
pipe_range = size//2

plus = "+"
minus = "-"
space = " "
pipe = "|"

#Make the top line
print(f'{plus}',end='')
print (f'{(space+minus)*dash_count}{space}{plus}'*2)

for box in range(2):
    for x in range(pipe_range):
        #Make all the middle lines
        print(f'{pipe}',end='')
        print (f'{space*size}{pipe}{space*size}{pipe}')
        
    #Make the bottom line
    print(f'{plus}',end='')
    print (f'{(space+minus)*dash_count}{space}{plus}'*2)


