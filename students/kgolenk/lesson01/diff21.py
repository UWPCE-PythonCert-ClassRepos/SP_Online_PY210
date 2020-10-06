# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
    if n <= 21:
        return abs(n - 21)
    else:
        return 2 * (abs(n - 21))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end(str):
  if len(str) >= 2:
    return str[len(str) - 2:]*3
  else:
    return str*3

# ===================================================================== #
# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer):
    if is_summer and temp >= 60 and temp <= 100:
        return True
    elif not is_summer and temp >= 60 and temp <= 90:
        return True
    else:
        return False
# ====================================================================== #
# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation,
# return a string of the form "7:00" indicating when the alarm clock should ring.
# Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
# Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
  if vacation:
    if day in range(1, 6):
      return "10:00"
    elif day == 0 or day == 6:
      return "off"
  else:
    if day in range(1, 6):
      return "7:00"
    elif day == 0 or day == 6:
      return "10:00"

# ===================================================================== #

