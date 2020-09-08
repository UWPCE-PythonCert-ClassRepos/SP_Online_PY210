def string_bits(str):
    wrd = ""
    n=0
    for i in str:
        n+=1
        if n== 0 or n%2!=0:
            wrd=wrd+i
    return wrd
    
    
def string_splosion(str):
  wrd=""
  k=""
  for i in str:
    wrd=wrd+i
    k+=wrd
  return k
