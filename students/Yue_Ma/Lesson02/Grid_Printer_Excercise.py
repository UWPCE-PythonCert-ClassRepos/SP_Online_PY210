def print_grid(n, units):
    x = '+ ' + '- ' * units
    y = '| ' + '  ' * units

    for j in range(0, n):
        print(x * n + '+')
        for i in range(0, units):
            print(y*n + '|')

    print(x * n + '+')
