def cigar_party(cigars, is_weekend):
  if is_weekend and cigars > 40:
    return True
  elif (cigars >=40) and (cigars <= 60):
      return True
  else:
      return False

def date_fashion(you, date):

    if you <=2 or date <=2:
        return 0
    elif you >= 8 or date >=8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    if is_summer and (temp >=60 and temp <=100):
        return True
    elif temp >=60 and temp <=90:
        return True
    else:
        return False

def caught_speeding(speed, is_birthday):
    if not is_birthday:
        if speed <= 60:
            return 0
        elif speed >= 61 and speed <=80:
            return 1
        else:
          return 2
    else:
        if speed <= 65:
            return 0
        elif speed >= 61 and speed <=85:
            return 1
        else:
            return 2

def sorta_sum(a, b):
    sum = a+b
    if sum >=10 and sum <=19:
        return 20
    else:
        return sum

def alarm_clock(day, vacation):
    if vacation and (day ==0 or day ==6):
        return 'off'
    elif vacation and (day >0 or day <6):
        return '10:00'
    elif not vacation and (day ==0 or day ==6):
        return '10:00'
    elif not vacation and (day >0 or day <6):
        return '7:00'

def love6(a, b):
    sum = a+b
    diff = abs(a-b)
    if a== 6 or b ==6:
        return True
    elif sum == 6 or diff == 6:
        return True
    else:
        return False

def in1to10(n, outside_mode):
    if outside_mode and (n <=1 or n >=10):
        return True
    elif not outside_mode and (n >=1 and n <=10):
        return True
    else:
        return False

def near_ten(num):
    if (num % 10) <= 2 or (num % 10) >= 8 :
        return True
    else:
        return False


if __name__ == "__main__":
    date_fashion(5, 10)
    cigar_party(30, False)
    squirrel_play(70, False)
    caught_speeding(60, False)
    sorta_sum(3, 4)
    alarm_clock(1, False)
    love6(6, 4)
    in1to10(5, False)
    near_ten(12)