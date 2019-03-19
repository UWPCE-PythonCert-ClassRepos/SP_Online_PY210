def print_grid(n): 
        print("+", end=" ")
        for i in range(n - 1):
            print("- - - - +",end =" ")
        print("- - - - +") 
        
           
def print_gridi(n): 
        print("|", end=" ")
        for i in range(n - 1):
            print("        |",end =" ")
        print("        |")


def grid(a,b):
        print_grid(a)
        for i in range(b):
                for i in range(4):
                        print_gridi(a)
                print_grid(a)

# Read user integer input for column and row then calls main function grid
a=int(input("Col: "))
b=int(input("Row: "))

grid(a,b)


#print_grid(4)
#print_grid1(4)

      
