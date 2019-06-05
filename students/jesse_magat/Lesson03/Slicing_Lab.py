def exchange_first_last(seq):
#Return sequence with first and last elements exchanged
    seq_first = seq[0:1]
    seq_last = seq[-1:]
    seq_middle = seq[1:-1]
    new_seq = seq_last + seq_middle + seq_first
    return new_seq

#exchange_first_last("this is a string")


def remove_everyother(seq):
    #Return sequence with every other item removed
    new_seq = seq[0:len(seq):2] #start with first character #remove every second character
    return new_seq

#remove_everyother("this is a string")

def remove_first4_last4(seq):
    new_seq = seq[4:-4:2]
    return new_seq
#remove_first4_last4("this is a string")


def backwards(seq):
    new_seq = seq[::-1]
    return new_seq
#backwards("this is a string")


def last_first_third_3chars(seq):
      
    # with the last third, then first third, then the middle third in new order
    
    third = int(len(seq)/3) # getting the third of total character  
    last_third = seq[-third:] # getting the last third of string
    first_third = seq[:third] #getting the first third of string  
    mid_1 = seq[third:]#remove first third chars
    mid_third = mid_1[:-third]#remove last third chars from mid_1
    
    new_seq = last_third + first_third + mid_third

    return new_seq
#last_first_third_3chars("this is a string")


seq = "this is a string" #identify string variable


if __name__ == "__main__":
    
    try:
        assert exchange_first_last(seq) =='ghis is a strint'
        assert remove_everyother(seq) =='ti sasrn'
        assert remove_first4_last4(seq) == ' sas'
        assert backwards(seq) == 'gnirts a si siht'
        assert last_first_third_3chars(seq) == 'tringthis is a s'
        print('Passed test')
    except:
        print('Failed test')



