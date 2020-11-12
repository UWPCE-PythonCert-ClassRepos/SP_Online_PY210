#print(dir(5))
# print(type(499))
# print(dir(__builtins__))

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(3))




