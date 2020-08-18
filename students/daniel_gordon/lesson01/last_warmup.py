def string_match(a, b):
  length = min(len(a),len(b))
  sum = 0
  for i in range(length-1):
    if a[i:i+2] == b[i:i+2]:
      sum += 1
  return sum