# Title: Break Me - Lesson 1 Python Puzzle Warmups
# Dev: Roslyn Melookaran
# Date: 8/24/20
# Change Log: (Who, When, What)
# R. Melookaran, 8/24/20, created script)
# --------------------------------------------------------------

# ----Warm Up 1.1---- #
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  elif weekday and not vacation:
    return False
  elif not weekday and vacation:
    return True
  else:
    return False

# ----Warm Up 1.2---- #
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  return False

# ----Warm Up 1.3---- #
def sum_double(a, b):
  if a!=b:
    sum = a + b
    return sum
  else:
    sum = (a+b)*2
    return sum

# ----Warm Up 1.4---- #
def diff21(n):
  if n>21:
    difference=2*(abs(21-n))
  else:
    difference = abs(21 - n)
  return difference

# ----Warm Up 1.5---- #
def parrot_trouble(talking, hour):
  if talking and hour>20:
    return True
  if talking and hour<7:
    return True
  else:
    return False

# ----Warm Up 1.6---- #
def makes10(a, b):
    sum = a + b
    if a == 10:
        return True
    elif b == 10:
        return True
    elif sum == 10:
        return True
    else:
        return False

# ----Warm Up 1.7---- #
def near_hundred(n):
  x=abs(n-100)
  y=abs(n-200)
  if x>10:
    if y>10:
      return False
    else:
      return True
  else:
    return True

# ----Warm Up 1.8---- #
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

# ----Warm Up 1.9---- #
def not_string(str):
  str2="not"
  z=str.find(str2)
  if z==0:
    return str
  else:
    str3=str2+" "+ str
    return str3

# ----Warm Up 1.10---- #
def missing_char(str, n):
  str=str[:n]+str[n+1:]
  return str

# ----Warm Up 1.11---- #
def front_back(str):
  n=len(str)
  if n<=1:
    return str
  else:
    str2=str[n-1]+str[1:n-1]+str[0]
    return str2

# ----Warm Up 1.12---- #
def front3(str):
  str=str[0:3]+str[0:3]+str[0:3]
  return str

# ----Warm Up 2.1---- #
def string_times(str, n):
  x=""
  for i in range(n):
    x=x+str
  return x

# ----Warm Up 2.2---- #
def front_times(str, n):
  str2=str[:3]
  x=""
  for i in range(n):
    x=x+str2
  return x

# ----Warm Up 2.3---- #
def string_bits(str):
  n=len(str)
  x=""
  for i in range(n):
    if i%2==0:
      x=x+str[i]
  return x

# ----Warm Up 2.4---- #
def string_splosion(str):
  x=""
  n=len(str)
  for i in range(n+1):
    x=x+str[:i]
  return x

# ----Warm Up 2.5---- #
def last2(str):
    # Screen out too-short string case.
    if len(str) < 2:
        return 0
    # last 2 chars, can be written as str[-2:]
    last2 = str[len(str) - 2:]
    count = 0
    # Check each substring length 2 starting at i
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1
    return count
