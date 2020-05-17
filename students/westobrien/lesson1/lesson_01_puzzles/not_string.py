def not_string(str):
  if str[:3] == "not":
    return str
  str = 'not ' + str
  return str