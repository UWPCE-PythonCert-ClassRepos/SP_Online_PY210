def sum_double(a, b):
  x = a+b
  if a==b:
    x*=2
  return x

def diff21(n):
  x = abs(n-21)
  if n>21:
    x*=2
  return x

def parrot_trouble(talking, hour):
  return(talking and (hour < 7 or hour > 20))