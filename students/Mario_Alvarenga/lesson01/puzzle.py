#Posted my solution from one of the warmups

def parrot_trouble(talking, hour):
  if talking and (hour< 7 or hour > 20):
    return True
  return False

parrot_trouble(8,5)
