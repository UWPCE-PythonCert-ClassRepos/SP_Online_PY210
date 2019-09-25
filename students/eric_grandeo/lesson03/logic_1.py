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




