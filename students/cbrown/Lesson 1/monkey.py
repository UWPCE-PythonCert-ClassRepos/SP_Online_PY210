#Warmup-Monkey Trouble

a_smile = False
b_smile = True


def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    else:
        return False

monkey_trouble(a_smile,b_smile)
