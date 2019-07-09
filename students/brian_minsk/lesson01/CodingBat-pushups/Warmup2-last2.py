def last2(str):
  strLast2 = str[len(str)-2:]
  nMatch = 0
  for i in range(len(str) - 3):
      strNext2 = str[i:i+2]
      if strNext2 == strLast2:
          nMatch = nMatch + 1
  return nMatch

print(last2("cbdabljafabwoiijab"))
