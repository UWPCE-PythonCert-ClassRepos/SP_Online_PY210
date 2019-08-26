def sleep_in(weekday, vacation):
    #if not weekday sleepin
    if weekday != True:
        return(True)
    elif vacation == True:
        return (True)
    else:
        return (False)

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return (True)
    else:
        return(False)

def sum_double(a,b):
    if a == b:
        c=(a+b)*2
    else:
        c=a+b
    return (c)

def diff21(n):
    val = n -21
    if n <=21:
        return (21-n)
    else:
        return (n-21)*2


def parrot_trouble(talking,hour):
    if talking and (hour > 20 or hour < 7):
        return True
    else:
        return False

def makes10(a,b):
    return(a==10 or b==10 or (a +b)==10)



print(sleep_in(False,False))
print(sleep_in(True,False))
print(sleep_in(False,True))

print("-------Monkey Trouble-------")

print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

print("-------double sum-------")
print (sum_double(1, 2))
print (sum_double(3, 2))
print (sum_double(2, 2))

print("-------diff-------")

print(diff21(19))
print(diff21(10))
print(diff21(50))











