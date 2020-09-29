#Warmup-1
#by ReemAlqaysi
""" this file includes many functions puzzle from codeingbat.com """

#sleep_in 
def sleep_in(weekday, vacation):
  if not weekday:
   return True
  elif vacation:
    return True
  else:
   return False


#diff21
def diff21(n):
  if n <= 21:
   result = 21-n
  else:
   result = (n-21)*2
  return result


# parrot_trouble 
def parrot_trouble(talking, hour):
 if talking and (hour <7 or hour >20):
   return True
 else:
   return False


#makes10
def makes10(a,b):
  if (a == 10) or (b == 10):
   return True
  elif (a+b) == 10:
   return True
  else:
   return False



#near_hundred 
def near_hundred(n):
 if ((abs(100-n) <= 10) or  (abs(200-n) <= 10)):
  return True
 else:
  return False



#not_string
def not_string(str):
  if str[0:3] == 'not':
    return str
  else:
    return ('not '+str)



#front3 
def front3(str):
  str = str[0:3]+str[0:3]+str[0:3]
  return str



#monkey_trouble 
def monkey_trouble(a_smile, b_smile):
  if (a_smile and  b_smile) or  (not a_smile and not b_smile):
    return True
  else:
    return False



#sum_double 
def sum_double(a, b):
  if a==b:
    return (a+b)*2
  else:
   return a+b


#pos_Neg
def pos_neg(a, b, negative):
 if negative and (a <0 and b < 0):
    return True
 elif not negative and  ((a <0 and b > 0) or (a>0 and b<0)):
    return True
 else:
    return False


#missing_char 
def missing_char(str, n):
    front = str[:n]
    back = str[n+1:]
    return front + back

#front_back 
def front_back(str):
  n = len(str)
  if n <= 1:
   return str
  elif n == 2:
    return str[n-1]+str[0]
  else:
    first = str[0]
    last = str[n-1]
    middle = str[1:(n-1)]
    return last+middle+first


if __name__ == "__main__":
    
  sleep_in(False,True)
  monkey_trouble(True,True)
  sum_double(1,2)
  diff21(21)
  parrot_trouble(True,6)
  makes10(9,10)
  near_hundred(93)
  pos_neg(1,-1,False)
  not_string('candy')
  missing_char('kitten',0)
  front_back('code')
  front3('Java')
