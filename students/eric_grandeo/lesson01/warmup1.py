#sleep in
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
print("Sleep in")
print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))
print('-' * 25)

#monkey trouble
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False    

print("Monkey Trouble")
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
print('-'*25)

#sum_double
def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return a+b

print("sum_double")
print(sum_double(1,2))
print(sum_double(3,2))
print(sum_double(2,2))
print('-' * 25)

#dif21
def diff21(n):
    diff = abs(21-n)
    return diff

print("diff21")
print(diff21(19))
print(diff21(10))
print(diff21(21))
print('-'*25)

#parrot trouble
def parrot_trouble(talking, hour):
    if talking and hour < 7 or hour > 20:
        return True
    else:
        return False    

print("parrot trouble")
print(parrot_trouble(True,6))
print(parrot_trouble(True,7))
print(parrot_trouble(False, 6))
print('-'*25)

#makes ten
def makes10(a,b):
    
    if a == 10 or b == 10:
        return True
    elif a+b == 10:
        return True
    else:
        return False
    
    
print("makes10")
print(makes10(9,10))
print(makes10(9,9))
print(makes10(1,9))
print('-'*25)

#near_hundred
def near_hundred(n):
    if 90 <= n <= 110:
        return True
    elif 190 <= n <= 210:
        return True
    else:
        return False

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
print('-'*25)

#pos_neg
def pos_neg(a, b, negative):
    '''
    if negative is True:
        if a < 0 and b < 0:
            return True
        else:
            return False    
    if negative is False:
        if a > 0 or b > 0:
            return True
        else:
            return False    
    '''
    if negative:
        return(a<0 and b<0)
    else:
        return((a < 0 and b>0) or (a >0 and b<0))

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
print('-'*25)

#not_string
def not_string(str):
    if str[:3] == "not":
        return str
    
    return "not " + str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))
print('-' * 25)

#missing char
def missing_char(str, n):
    new_str = str.replace(str[n],"")
    return new_str

print(missing_char('kitten',1))
print(missing_char('kitten',0))
print(missing_char('kitten',4))
print('-'*25)    

#front_back
def front_back(str):
    if len(str) == 1:
        return str
    front = str[0]
    back = str[-1]
    new_string = back + str[1:-1] + front

    return new_string

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
print('-'*25)

#front3
def front3(str):
    if len(str) < 3:
        return str
    new_str = str[:3] * 3
    return new_str

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))





    




