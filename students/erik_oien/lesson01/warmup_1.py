# sleep_in

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# monkey_trouble

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

# sum_double

def sum_double(a, b):
  sum = a+b
  if a == b:
    return sum * 2
  return sum

# diff21

def diff21(n):
  if n <= 21:
    return 21 - n
  return abs(21 - n) * 2

# parrot_trouble

def parrot_trouble(talking, hour):
  if talking:
    if 7 <= hour <= 20:
      return False
    else:
      return True
  return False

# makes10

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  return False

# near_hundred

def near_hundred(n):
  return(abs(n-100) <= 10 or abs(n-200) <= 10)

# pos_neg

def pos_neg(a, b, negative):
  if negative:
    if a < 1 and b < 1:
      return True
    else:
      return False
  if (a < 1 and b >= 1) or (a >= 1 and b < 1):
    return True
  return False

# not_string

def not_string(str):
  if str[0:3] == "not":
    return str
  return "not " + str

# missing_char

def missing_char(str, n):
  return str[:n] + str[n+1:]

# front_back

def front_back(str):
  if len(str) <= 1:
    return str
  return str[len(str)-1] + str[1:-1] + str[0]  

# front3

def front3(str):
  if len(str) < 3:
    return str + str +str
  new_str = str[0:3]
  return new_str + new_str + new_str