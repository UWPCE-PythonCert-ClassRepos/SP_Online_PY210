#Excersises: Python Pushups

#Warmup-1

#Monkey_Trouble
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False

#Sum_Double
def sum_double(a, b):
    if a == b:
        return 2*(a+b)
    return (a+b)

#diff21
def diff21 (n):
    if n <=21 :
        return abs(21-n)
    if n>21 :
        return 2* abs(21-n)

#makes10
def makes10(a, b):
    if a==10 or b == 10:
        return True
    if a+b == 10:
        return True
    return False

#front 3
def front3(str):
    a = len(str)
    front = str[:3]
    if a < 3:
        return str + str +str
    return front + front + front

