		
#diff21
def diff21(n):
    if abs(n - 21) <= 21:
	    return abs(n - 21)
	else:
	    return 2 * (abs(n - 21))


#near_hundred
def near_hundred(n):
    if 90 <= abs(n) < 100 or 190 <= abs(n) < 200:
        return True
    else:
        return False

