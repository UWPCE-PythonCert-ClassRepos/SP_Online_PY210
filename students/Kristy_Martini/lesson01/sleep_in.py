def sleep_in(weekday, vacation):
  if vacation: 
      return True
  elif not weekday and not vacation:
      return True
  elif weekday and not vacation:
      return False