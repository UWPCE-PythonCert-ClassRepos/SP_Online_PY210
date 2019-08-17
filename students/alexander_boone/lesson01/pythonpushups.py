def front_times(str, n):
  
    s = ''
    
    if len(str) < 3:
      front = str
    else:
      front = str[0:3]
    
    for i in range(n):
      s = s + front
      
    return s