def front3(str):
  if len(str) <= 3:
    return str+str+str
  front = str[:3]
  return front+front+front