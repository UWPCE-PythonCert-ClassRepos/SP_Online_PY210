def print_grid1(n):
    '''
    Prints a grid of size n
    '''
    print('+ '+' - '*n+' + '+' - ' *n+' +')
    print('| ' + '   ' * n + ' | ' + '   ' * n + ' |')
    print('| ' + '   ' * n + ' | ' + '   ' * n + ' |')
    print('| ' + '   ' * n + ' | ' + '   ' * n + ' |')
    print('+ ' + ' - ' * n + ' + ' + ' - ' * n + ' +')
    print('| ' + '   ' * n + ' | ' + '   ' * n + ' |')
    print('| ' + '   ' * n + ' | ' + '   ' * n + ' |')
    print('| ' + '   ' * n + ' | ' + '   ' * n + ' |')
    print('+ ' + ' - ' * n + ' + ' + ' - ' * n + ' +')

def print_grid2(n1,m):
    '''
    prints n rows and n columns of grid of size m
    '''
    tmp = m
    str1 = '+ ' + ' - ' * n1 + ' + '
    str2 = ' - ' * n1 + ' + '
    str3 = '| ' + '   ' * n1 + ' | '
    str4 = '   ' * n1 + ' | '
    final_str1, final_str2 = '',''
    while m:
        final_str1 = ''
        for i in range(tmp):
            if i == 0:
                final_str1 += str1
            else:
                final_str1 += str2
        print(final_str1)
        tmp2 = n1
        while tmp2:
            final_str2 = ''
            for i in range(tmp):
                if i == 0:
                    final_str2 += str3
                else:
                    final_str2 += str4
            print(final_str2)
            tmp2 -= 1
        if m == 1:
            print(final_str1)
        m -= 1

if __name__ == '__main__':
    # Grid size of one parameter
    n = int(input("Enter grid size: "))
    print_grid1(n)

    # Grid size of two parameters
    m = int(input("Enter number of times to repeat: "))
    n1 = int(input("Enter grid size: "))
    print_grid2(n1, m)
