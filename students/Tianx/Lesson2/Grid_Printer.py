def print_grid(n, m):
    def horizontal():
        # Build String
        # print_ln = plus+cell_size*minus+plus+cell_size*minus+plus
        print_ln = plus
        for c in range(n):
            print_ln = print_ln + cell_size * minus + plus
        print(print_ln)

    def vertical():
        for p in range(cell_size):
            # print_ln = bar+cell_size*space+bar+cell_size*space+bar
            print_ln = bar
            for c in range(n):
                print_ln = print_ln + cell_size * space + bar

            print(print_ln)

    n = round(n)
    m = round(m)
    plus = '+ '
    minus = '- '
    space = '  '
    bar = '| '
    cell_size = m
    # print(cell_size)
    horizontal()
    for q in range(n):
        vertical()
        horizontal()


if __name__ == '__main__':
    print('******* Start Main *******')

    print_grid(3, 4)
    # print_grid(5,3)
    print_grid(3.3, 4.5)
    print_grid(3.8, 4.9)
