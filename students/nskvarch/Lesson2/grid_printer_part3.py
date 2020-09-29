#Part 3 of the grid printer exercise, created by Niels Skvarch
#I kept having a duplicate vertical or horizontal line created when adding additional coloumns and rows until I spent some time with Google
#and a co-worker who taught me about the join operator, with that I was able to create this successfully. 

def print_grid(size, count):
    for i in range(count):
        print_horizontal_line(size, count)
        print_vertical_line(size, count)
    print_horizontal_line(size, count)


def print_horizontal_line(size, count):
    print(get_horizontal_line(size, count))


def get_horizontal_line(size, count):
    return "+%s+" % ("+".join(["-" * size for _ in range(count)]))


def print_vertical_line(size, count):
    string = get_vertical_line(size, count)
    for _ in range(size):
        print(string)


def get_vertical_line(size, count):
    return "|%s|" % ("|".join([" " * size for _ in range(count)]))


size = int(input("what size grid would you like?: "))
count = int(input("How many rows and coloumns would you like?: "))
print_grid(size, count)



