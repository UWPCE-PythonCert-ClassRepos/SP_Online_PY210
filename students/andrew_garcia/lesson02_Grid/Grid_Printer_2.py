'''
Andrew Garcia
Grid Printer 2
6/2/19
'''

def print_grid(size):
    def horizontal_line():
        print('+', end='')
        print(' - '*(size // 2), end='')  # divides section into 2 for middle divider
        print('+', end='')
        print(' - ' * (size // 2), end='')
        print('+')

    def vertical_line():
        for number in range(size // 2):
            print('|', end='')
            print('   ' * (size // 2), end='')
            print('|', end='')
            print('   ' * (size // 2), end='')
            print('|')

    def create_grid():
        horizontal_line()
        vertical_line()
        horizontal_line()
        vertical_line()
        horizontal_line()

    create_grid()


print_grid(int(input("Enter a number: ")))
