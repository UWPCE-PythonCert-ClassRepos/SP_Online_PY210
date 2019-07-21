#Warmup
#by ReemAlqaysi
#sleep_in 
def sleep_in(weekday, vacation):
  if not weekday:
   return True
  elif vacation:
    return True
  else:
   return False
sleep_in(False, False)


#diff21
def diff21(n):
  if n <= 21:
   result = 21-n
  else:
   result = (n-21)*2
  return result
diff21(16)


# parrot_trouble 
def parrot_trouble(talking, hour):
 if talking and (hour <7 or hour >20):
   return True
 else:
   return False
parrot_trouble(true,3)

#makes10
def makes10(a,b):
  if (a == 10) or (b == 10):
   return True
  elif (a+b) == 10:
   return True
  else:
   return False
makes10(4,6)



#near_hundred 
def near_hundred(n):
 if ((abs(100-n) <= 10) or  (abs(200-n) <= 10)):
  return True
 else:
  return False
near_hundred(97)


#not_string
def not_string(str):
  if str[0:3] == 'not':
    return str
  else:
    return ('not '+str)
not_string('cute')


#front3 
def front3(str):
  str = str[0:3]+str[0:3]+str[0:3]
  return str
not_string(abc)


#monkey_trouble 
def monkey_trouble(a_smile, b_smile):
  if (a_smile and  b_smile) or  (not a_smile and not b_smile):
    return True
  else:
    return False
monkey_trouble(True,True)


#sum_double 
def sum_double(a, b):
  if a==b:
    return (a+b)*2
  else:
   return a+b
sum_double(2,5)



