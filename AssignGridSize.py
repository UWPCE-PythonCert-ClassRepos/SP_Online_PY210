def grid_input():
    while True:
        try:
            grid_space = int(input("input grid size\n"))
            if grid_space<2:
                print("invalid integer")
            else:
                return grid_space
        except ValueError:
                print("invalid input")


def print_gridinput():
    length=grid_input()
    width=length
    for n in range(length):
        print(("+" + "-" * width) * length + "+")
        for n in range(length):
            print(("|" + " " * width) * length + "|")
            print(("+" + "-" * width) * length + "+")
        break

print_gridinput()

