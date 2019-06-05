 #n = 9
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +



def line_style_1(n):
    print('+',end='')
    for i in range(0,n):
        if i ==n//2:
            print(' +', end='')
        else:
            print(' -',end='')

    print(' +')


def line_style_2(n):
    print('|',end='')
    for i in range(0,n):
        if i ==n//2:
            print(' |', end='')
        else:
            print(2*' ',end='')

    print(' |')


def grid(n):
    print()
    line_style_1(n)
    for i in range(0,n):
        if i ==n//2:
            line_style_1(n)
        else:
            line_style_2(n)
    line_style_1(n)


if __name__ == "__main__":
    grid(9)

