#cigar_party

def cigar_party(cigars, is_weekend):
    if not is_weekend:
        return 40 <= cigars <= 60
    else:
        return is_weekend and cigars > 40

assert cigar_party(30, False) == False
assert cigar_party(50, False) == True
assert cigar_party(70, True) == True
print("Cigar party tests passed")



#date_fashion

def date_fashion(you, date):
    if you <= 2 or date <= 2: 
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

assert date_fashion(5, 10) == 2
assert date_fashion(5, 2) == 0
assert date_fashion(5, 5) == 1
print("date fashion tests passed")

#squirrel_play





