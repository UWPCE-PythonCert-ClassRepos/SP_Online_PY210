#--------------------------
#Title: Slicing Lab
#Description: Write various functions involving sequence slicing
#Original Dev: Lee Deitesfeld
#Change Log:
#20190404LAD Created functions
#--------------------------

def exchange_first_last(seq):
    '''Takes a sequence as an argument, and returns the first and
       last items exchanged'''
    #if a list sequence
    if type(seq) == list:
        #remove last item of list
        last = seq.pop()
        #remove first item of list
        first = seq.pop(0)
        #add first item to end of list
        seq.append(first)
        #add last item to beginning of list
        seq.insert(0, last)
        #print final list
        return seq
    #elif a tuple sequence
    elif type(seq) == tuple:
        #create list from tuple seq
        list_from_tuple = list(seq)
        #remove last item of list
        last = list_from_tuple.pop()
        #remove first item of list
        first = list_from_tuple.pop(0)
        #add first item to end of list
        list_from_tuple.append(first)
        #add last item to beginning of list
        list_from_tuple.insert(0, last)
        #create tuple from generated list
        final_tuple = tuple(list_from_tuple)
        return final_tuple
    #elif a string sequence
    elif type(seq) == str:
        first = seq[0]
        last = seq[-1]
        middle = seq[1:-1]
        #concatenate last letter, middle letter(s), first letter
        final_string = last + middle + first
        return final_string

def del_every_other(seq, n = 2):
    '''Takes a sequence, and returns sequence with every other item removed'''
    #convert sequence into a list
    lst_sequence = list(seq)
    #sequence including every other item
    lst_final = lst_sequence[::n]
    #if sequence is a string, convert lst_final back into a string
    if type(seq) == str:
        str_final = "".join(str(x) for x in lst_final)
        return str_final
    #if sequence is a tuple, convert lst_final back into a tuple
    elif type(seq) == tuple:
        tuple_final = tuple(lst_final)
        return tuple_final
    #if sequence is a list, return lst_final
    else:
        return lst_final

def frst_lst_4_evry_othr(seq, n=2):
    '''Takes a sequence, removes first and last four items, as well as every
    other item in between'''
    #convert sequence into a list
    lst_sequence = list(seq)
    #remove first four items
    lst_first = lst_sequence[4:]
    #remove last four items
    lst_last = lst_first[:-4]
    #return every other letter of leftover list
    lst_final = lst_last[::n]
    #if sequence is a string, convert lst_final back into a string
    if type(seq) == str:
        str_final = "".join(str(x) for x in lst_final)
        return str_final
    #if sequence is a tuple, convert lst_final back into a tuple
    elif type(seq) == tuple:
        tuple_final = tuple(lst_final)
        return tuple_final
    #if sequence is a list, return lst_final
    else:
        return lst_final

def reversed(seq):
    '''Take a sequence and return the items in reverse order'''
    return seq[::-1]

def thirds(seq):
    '''Take a sequence, and return with the last third, then first third,
        then the middle third in the new order'''
    first_third = seq[:3]
    middle_third = seq[3:6]
    last_third = seq[6:]
    seq_final = last_third,first_third,middle_third
    return seq_final

#-----------------assertion tests----------------#
if __name__ == "__main__":

    #tests for exchange_first_last()
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    #tests for del_every_other()
    bread = 'bread'
    lst_123456 = [1,2,3,4,5,6]
    assert del_every_other(bread) == 'bed'
    assert del_every_other(lst_123456) == [1,3,5]

    #tests for frst_lst_4_evry_othr()
    longstring = '123456781234'
    longtuple = ((1,2,3,4,5,6,7,8,1,2,3,4))
    assert frst_lst_4_evry_othr(longstring) == '57'
    assert frst_lst_4_evry_othr(longtuple) == (5,7)

    #tests for reversed()
    hello = 'hello' == 'olleh'
    lst_dogs = ['spaniel','retriever','bulldog'] == ['bulldog','retriever','spaniel']

    #tests for thirds()
    str_123 = '123456789'
    lst_123 = [1,2,3,4,5,6,7,8,9]
    assert thirds(str_123) == ('789', '123', '456')
    assert thirds(lst_123) == ([7, 8, 9], [1, 2, 3], [4, 5, 6])

    print("tests passed")
