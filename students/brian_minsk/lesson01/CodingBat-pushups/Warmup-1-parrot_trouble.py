def parrot_trouble(talking, hour):
    if not talking:
        return False
    else:
        if hour < 7 or hour > 20:
            return True
        else:
            return False

print (parrot_trouble(True, 6))
  