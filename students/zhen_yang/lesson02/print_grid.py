# printing a grid
def print_grid(num):
    tot_num = num + 2
    even_num = (num + 1 ) % 2
    if even_num  == 0:
        the_num = (num+1)/2
        for i in range(0,tot_num):
            #if i == 0 or i == num + 1 or i == 10:
            if i % the_num == 0:
                for j in range(0,tot_num):
                    if j % the_num  == 0 :
                        print(" +",end = "")
                    else:
                        print(" -",end = "")
                print("\n")
            else :
                for j in range(0,tot_num):
                    if j % the_num == 0 :
                        print(" |",end = "")
                    else:
                        print("  ", end = "")
                print("\n")
    else:
        print(f"Something is wrong! the num {num} for grid has to be an odd num.")
        exit()

# calling the print_grid()
#print_grid(9)
#print_grid(3)
#print_grid(15)

# print_grid_2()
def print_grid_2 (row_col_num, unit_size):
    tot_num = ( row_col_num * unit_size ) + row_col_num + 1
    the_num =  unit_size + 1
    for i in range(0,tot_num):
        if i % the_num == 0:
            for j in range(0,tot_num):
                if j % the_num  == 0 :
                    print(" +",end = "")
                else:
                    print(" -",end = "")
            print("\n")
        else :
            for j in range(0,tot_num):
                if j % the_num == 0 :
                    print(" |",end = "")
                else:
                    print("  ", end = "")
            print("\n")


# calling the print_grid_2()
row_col_num = 5 
unit_size = 3 
print(f"For row/col {row_col_num}  unit size: {unit_size}")
print_grid_2(row_col_num,unit_size)
