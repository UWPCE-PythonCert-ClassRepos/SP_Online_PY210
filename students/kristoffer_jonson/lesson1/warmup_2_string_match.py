def string_match(a, b):
  length = len(a)
  if len(a) > len(b):
    length = len(b)
  count = 0
  for i in range(length-1):
    if a[i:i+2] == b[i:i+2]:
      count = count +1
  return count
