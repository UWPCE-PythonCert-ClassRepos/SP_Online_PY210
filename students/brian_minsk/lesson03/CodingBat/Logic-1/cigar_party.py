def cigar_party(cigars, is_weekend):
    return (cigars >= 40 and cigars =< 60) or (is_weekend and cigars >= 40)

if __name__ == "__main__":
    # run some tests
    assert cigar_party(30, False) == False
    assert cigar_party(50, False) == True
    assert cigar_party(70, True) == True
    