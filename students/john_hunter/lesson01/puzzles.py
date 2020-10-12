##John Hunter, Doing Python Pushups

##Monkey Trouble
def monkey_trouble(a_smile, b_smile):
  return a_smile==b_smile

##Sleep In
def sleep_in(weekday, vacation):
  return vacation or not weekday

## diff on 21
def diff21(n):
  if n > 21:
    n=(n-21)*2
    return n 
  elif n < -21:
    n=abs(21+n)
    return n
  else :
    n=21-n
    return n
  
## Btween two hundreds
def near_hundred(n):
    return 89<n<111 or 189<n<211

##Missing Char, this works in Spyder but not on coding bat?

str = 'kitten'
n = 4

def missing_char(str, n):
  result_str = ""
  for i in range(0, len(str)):
    if i !=n:
      result_str = result_str + str[i] 
  print(result_str)
missing_char(str, n) 

##Parrot Trouble
def parrot_trouble(talking, hour):
  return talking and 7>hour or talking and 20<hour


## Negative Positive
def pos_neg(a, b, negative):
  if negative and (a<0 and b<0):
    return True
  if (a<0 and 0<b) and not negative:
    return True
  if (b<0 and 0<a) and not negative:
    return True
  else :
    return False

## Switch First and Last brute force
def front_back(str):
  if len(str)==0:
    return str
  if len(str)==1:
    return str
  if len(str)==2:
    newStr=str[::-1]
    str=newStr
    return str
  else :
    newStr=str[1:-1]
    first=str[0]
    last=str[-1]
    str=last + newStr + first
    return str


##Summy
def sum_double(a, b):
  if a==b:
    return 2*(a+b)
  else:
    return a+b

## Tens
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  if a+b==10:
    return True
  else:
    return False

## Knot String
def not_string(str):
  if str[:3]=='not':
    return str
  else:
    str = 'not '+str
    return str

##3 fronts
def front3(str):
  newStr=str[:3]*3
  return newStr

