def sleep_in(weekday, vacation):
  if vacation: return True
  if weekday: return False
  return True;

print(sleep_in(False, True));