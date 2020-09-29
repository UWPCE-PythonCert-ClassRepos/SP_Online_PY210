        
#diff21
def diff21(n):
    if abs(n - 21) <= 21:
        return abs(n - 21)
    else:
        return 2 * (abs(n - 21))


#near_hundred
def near_hundred(n):
    if 90 <= abs(n) < 100 or 190 <= abs(n) < 200:
        return True
    else:
        return False
        
#monkey_trouble
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
 
#parrot_trouble
def parrot_trouble(talking, hour):
    if talking == True:
        if 7 > hour or hour > 20:
            return True
        else:
            return False
    else:
        return False

#pos_neg
def pos_neg(a, b, negative):
   