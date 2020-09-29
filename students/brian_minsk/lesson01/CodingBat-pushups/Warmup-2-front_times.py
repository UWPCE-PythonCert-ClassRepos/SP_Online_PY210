def front_times(str, n):
  strTimes = str[:3]
  for i in range(n - 1):
      strTimes = strTimes + str[:3]
  return strTimes

print(front_times("foobar", 5))