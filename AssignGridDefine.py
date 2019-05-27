def ask_length():
    while True:
        try:
            grid_length = int(input("Input Grid Rows\n"))
            if grid_length<2:
                print("invalid integer")
            else:
                return grid_length
        except ValueError:
                print("invalid input")

def ask_width():
    while True:
        try:
            grid_width = int(input("Input Grid Columns\n"))
            if grid_width<2:
                print("invalid integer")
            else:
                return grid_width
        except ValueError:
                print("invalid input")

def print_gridinput():
    width= ask_width()
    length= ask_length()
    for n in range(width):
        print(("+" + "-" * length) * width + "+")
        for n in range(length):
            print(("|" + " " * length) * width + "|")
            print(("+" + "-" * length) * width + "+")
        break

print_gridinput()
