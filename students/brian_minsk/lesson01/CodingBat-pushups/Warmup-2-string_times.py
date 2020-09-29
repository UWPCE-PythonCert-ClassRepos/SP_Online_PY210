def string_times(str, n):
  strTimes = str
  for i in range(n - 1):
      strTimes = strTimes + str
  return strTimes

print(string_times("dog", 5))