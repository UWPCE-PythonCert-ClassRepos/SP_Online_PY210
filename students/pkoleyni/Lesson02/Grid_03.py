def plus():
    print('+ ', end='')
def space():
    print(' ', end='')
def dash():
    print('- ',end='')
def bar():
    print('| ',end='')

def repeat(n,f):
    for i in range(0,n):
        f()

def line_style_1(n,m):
    for i in range(0,n):
        plus()
        for i in range(0,m):
            dash()
    plus()
    print()

def line_style_2(n,m):
    for i in range(0,n):
        bar()
        for i in range(0,m):
            repeat(2,space)
    bar()
    print()


def result(n,m):
    line_style_1(n,m)
    for i in range(0,n):
        for i in range(0, m):
            line_style_2(n, m)
        line_style_1(n, m)



if __name__ == "__main__":
    result(3, 3)
