def not_string(str):
  if str.startswith("not"):
    return str
  else:
    str = "not " + str
    return str