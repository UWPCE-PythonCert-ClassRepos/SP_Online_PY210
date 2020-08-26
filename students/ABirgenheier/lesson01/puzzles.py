print('Warmup-1>makes10')
print('Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.')
print('Function is: makes10(a,b)')


def makes10(a, b):
    if (a == 10 or b == 10) or a+b == 10:
        return True
    else:
        return False


def pos_neg(a, b, negative):
    if negative == False and ((a >= 0 and b < 0) or (b >= 0 and a < 0)):
        return True
    elif negative == True and (a < 0) and (b < 0):
        return True
    else:
        return False


def not_string(str):
    if str[:3] == 'not':
        return str
    else:
        return 'not ' + str

# 'Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).')


def missing_char(str, n):
    newstr = str[:n] + str[n+1:]
    return newstr


'''
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. Return 
a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
'''


def front3(str):
    front = str[:3]
    fr3 = 3*front
    return fr3
