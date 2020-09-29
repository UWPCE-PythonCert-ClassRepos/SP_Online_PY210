def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def delete_every_other(seq):
    return seq[::2]

def delete_every_other_from_middle(seq):
    return seq[4:-4:2]

def my_reverse(seq):
    return seq[::-1]

def course_shuffle(seq):
    third = len(seq)//3
    return seq[-third:] + seq[:-third]
    

if __name__ == "__main__":
    a_string = "a random collection of words"
    a_tuple  = (4, 17, 20, 1, 18, 10)
    a_list   = [7, 3, 15, 12, 19, 0]
    
    assert exchange_first_last(a_string) == "s random collection of worda"
    assert exchange_first_last(a_tuple)  == (10, 17, 20, 1, 18, 4)
    assert exchange_first_last(a_list)   == [ 0, 3, 15, 12, 19, 7]
    
    assert delete_every_other(a_string) == "arno olcino od"
    assert delete_every_other(a_tuple)  == (4, 20, 18)
    assert delete_every_other(a_list)   == [7, 15, 19]
    
    assert delete_every_other_from_middle(a_string) == "no olcino "
    assert delete_every_other_from_middle(a_tuple)  == ()
    assert delete_every_other_from_middle(a_list)   == []
    
    assert my_reverse(a_string) == "sdrow fo noitcelloc modnar a"
    assert my_reverse(a_tuple)  == (10, 18, 1, 20, 17, 4)
    assert my_reverse(a_list)   == [0, 19, 12, 15, 3, 7]
    
    assert course_shuffle(a_string) == " of wordsa random collection"
    assert course_shuffle(a_tuple)  == (18, 10, 4, 17, 20, 1)
    assert course_shuffle(a_list)   == [19, 0, 7, 3, 15, 12]
    
    print("Test of slicing lab successful")