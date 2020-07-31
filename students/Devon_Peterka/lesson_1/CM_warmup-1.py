#!/usr/bin/env python3

#functions requested in exercise
def sleep_in(weekday, vacation):
	return (True if weekday == False or vacation == True else False)

def monkey_trouble(a_smile, b_smile):
	return (True if a_smile == b_smile else False)

def sum_double(a, b):
	sum = a+b
	return (2*sum if a == b else sum)

def diff21(n):
	return(21-n if n<=21 else 2*(n-21))

def parrot_trouble(talking, hour):
	if talking == True:
		return (False if hour in (7,20) else True)
	else:
		return False

def makes10(a, b):
	return (True if a == 10 or b == 10 or a+b == 10 else False)

def near_hundred(n):
	return (True if abs(200 - n) <= 10 or abs(100-n) <=10 else False)

def pos_neg(a, b, negative):
	if negative == True:
		return (True if a<0 and b<0 else False)
	else:
		if a>=0 and b<0:
			return (True)
		elif a<0 and b>=0:
			return (True)
		else:
			return (False)

def not_string(str):
	trigger = 'not'
	if str[0:len(trigger)] == trigger:
		return (str)
	else:
		return (trigger + ' ' + str)

def missing_char(str, n):
	if n>=0 and n<len(str):
		if n==0:
			return (str[1:len(str)])
		else:
			return (str[0:n] + str[n+1:len(str)])
	else:
		return ("Nothing to omit")

def front_back(str):
	if len(str) == 1:
		return (str)
	elif len(str) == 2:
		return (str[1] + str[0])
	else:
		return (str[len(str)-1] + str[1:len(str)-1] + str[0])

def front3(str):
	return(3*str if len(str) < 3 else 3*str[0:3])

#printed example outputs for each function
print('sleep_in(weekday, vacation)')
print('        ( False ,  False  ) ==> ',sleep_in(False, False))
print('        (  True ,  False  ) ==> ',sleep_in(True, False))
print('        ( False ,   True  ) ==> ',sleep_in(False, True))
print()
print('monkey_trouble(a_smile, b_smile)')
print('              (  True ,  True  ) ==> ', monkey_trouble(True, True))
print('              ( False , False  ) ==> ', monkey_trouble(False, False))
print('              (  True , False  ) ==> ', monkey_trouble(True, False))
print('              ( False ,  True  ) ==> ', monkey_trouble(False, True))
print()
print('sum_double(a, b)')
print('          (1, 2) ==> ', sum_double(1, 2))
print('          (3, 2) ==> ', sum_double(3, 2))
print('          (2, 2) ==> ', sum_double(2, 2))
print()
print('diff21( n )')
print('      (19 ) ==> ',diff21(19))
print('      (10 ) ==> ',diff21(10))
print('      (21 ) ==> ',diff21(21))
print('      (50 ) ==> ',diff21(50))
print()
print('parrot_trouble(talking, hour)')
print('              ( True  ,   6 ) ==> ',parrot_trouble(True, 6))
print('              ( True  ,   7 ) ==> ',parrot_trouble(True, 7))
print('              (False  ,   6 ) ==> ',parrot_trouble(False,6))
print()
print('makes10( a, b)')
print('       ( 9,10) ==> ',makes10(9,10))
print('       ( 9, 9) ==> ',makes10(9,9))
print('       ( 1, 9) ==> ',makes10(1,9))
print()
print('near_hundred( n )')
print('            ( 93) ==> ',near_hundred(93))
print('            ( 90) ==> ',near_hundred(90))
print('            ( 89) ==> ',near_hundred(89))
print('            (192) ==> ',near_hundred(192))
print()
print('pos_neg( a, b, negative);=')
print('       ( 1,-1,   False ) ==> ',pos_neg(1,-1,False))
print('       (-1, 1,   False ) ==> ',pos_neg(-1,1,False))
print('       (-4,-5,    True ) ==> ',pos_neg(-4,-5,True))
print()
print('not_string(str)')
print("      ('candy') ==> ",not_string('candy'))
print("          ('x') ==> ",not_string('x'))
print("    ('not bad') ==> ",not_string('not bad'))
print()
print('missing_char(   str  , n)')
print("            ('kitten', 1) ==> ",missing_char('kitten',1))
print("            ('kitten', 0) ==> ",missing_char('kitten',0))
print("            ('kitten', 4) ==> ",missing_char('kitten',4))
print("            ('kitten', 8) ==> ",missing_char('kitten',8))
print("            ('kitten',-4) ==> ",missing_char('kitten',-4))
print()
print('front_back(  str )')
print("          ('code') ==> ",front_back('code'))
print("          (   'a') ==> ",front_back('a'))
print("          (  'ab') ==> ",front_back('ab'))
print()
print('front3(    str    )')
print("      (     'Java') ==> ",front3('Java'))
print("      ('Chocolate') ==> ",front3('Chocolate'))
print("      (      'abc') ==> ",front3('abc'))
print()
