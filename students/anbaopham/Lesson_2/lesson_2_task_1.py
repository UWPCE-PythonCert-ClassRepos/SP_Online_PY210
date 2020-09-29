def print_grid(x):
    a = (x-1)//2
    for i in range(x+2):
        if i ==0:
            print("+" + "-"*a + "+" + "-"*a + "+")
        elif i == a+1:
            print("+" + "-"*a + "+" + "-"*a + "+")
        elif i == x+1:
            print("+" + "-"*a + "+" + "-"*a + "+", end= ' ')
        else:
            print("|" + " "*a + "|"+ " "*a + "|")


def print_grid2(c,x):
    a = (x-1)//2
    line_1 = ("+" + "-"*x)*(c-1) + ("+" + "-"*x+"+")
    line_2 = ("|"+ " "*x)*(c-1) + ("|") + " "*x + "|")
    for i in range(3*x+2):
        if i ==0:
            print(line_1)
        if i == x:
            print(line_1)
        else:
            print(line_2)


def print_grid2(c,x):
    a = c*x+c+2
    line_1 = ("+" + "-"*x)*(c-1) + ("+" + "-"*x+"+")
    line_2 = ("|" + " "*x)*(c-1) + ("|" + " "*x+"|")
    b = 1
    for i in range(1,a,1):

        if i ==1:
            print(line_1)

        elif i== x+1+b:
            print(line_1)
            b = i

        else:
            print(line_2)

def FizzBuzz(x=100):
    for i in range(1,x,1):
        if i%3 == 0:
            print("Fizz")
        elif i%5 ==0:
            print("Buzz")
        else:
            print(i)
