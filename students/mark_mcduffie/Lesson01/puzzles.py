#Warmup1
# 1
def sleep_in(weekday, vacation):
  if(not weekday or vacation):
    return True
  else:
    return False
# 2
def monkey_trouble(a_smile, b_smile):
  if(a_smile and b_smile):
    return True
  elif(not a_smile and not b_smile):
    return True
  else:
    return False
#3
def sum_double(a, b):
  if(a != b):
    return a + b
  else:
    return 2 * (a + b)
#4
def diff21(n):
  if(n <= 21):
    return 21-n
  else:
    return 2 * (n - 21)
#5
def parrot_trouble(talking, hour):
  if(hour < 7 and talking or hour > 20 and talking):
    return True
  else:
    return False
    
#Warmup2
#1
def string_times(str, n):
  result = ""
  for i in range(n):
    result +=  str
  return result
#2
def front_times(str, n):
  front = 3
  if front > len(str):
    front = len(str)
  frontNew = str[:front]
  result = ""
  for i in range(n):
    result = result + frontNew
  return result
#3
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result +=str[i]
  return result
#4
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result += str[: i + 1]
  return result
#5
def last2(str):
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count
#logic1
def cigar_party(cigars, is_weekend):
  if not is_weekend and 40 <= cigars <= 60:
    return True
  elif is_weekend and cigars >= 40:
    return True
  else:
    return False

def sorta_sum(a, b):
  if 9 < (a+b) < 20:
    return 20
  else:
    return a + b