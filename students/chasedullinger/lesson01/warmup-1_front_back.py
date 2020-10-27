# PY210 Lesson 01 - Chase Dullinger

def front_back(str):
  if len(str)<2:
    return str
  else:
    return str[-1]+str[1:len(str)-1]+str[0]
