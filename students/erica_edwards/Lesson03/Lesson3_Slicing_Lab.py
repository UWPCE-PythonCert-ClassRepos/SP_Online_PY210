def exchange_first_last(sequence):
    a = sequence[-1:]  
    b = sequence[1:-1]  
    c = sequence[0:1]
    result = a + b + c
    return result

def every_other_item(sequence):
    result = sequence[0:-1:2]
    return result

def first_last_middle(sequence):
    x = int(len(sequence)/3)
    result = sequence[x:-x:2]
    return result

def reverse_it(sequence):
    result = sequence[::-1]
    print(result)
    return result

def scramble(sequence):
    x = int(len(sequence)/3)
    result = sequence[x:] + sequence[0:x]
    print(result)
    return result

if __name__ == "__main__":
    #exchange_first_last('yo or do not, there is no trD')
    #every_other_item([1,2,3,4,5,6])
    #first_last_middle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    #reverse_it('there is no try')
    #scramble([1,2,3,4,5,6])

    a_string = 'do or do not'
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == 'to or do nod'
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert every_other_item(a_string) == 'd rd o'
    assert every_other_item(a_tuple) == (2, 13, 5)
    assert first_last_middle(a_string) == 'rd' 
    assert first_last_middle(a_tuple) == (13,)
    assert reverse_it(a_string) == 'ton od ro od'
    assert reverse_it(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert scramble(a_string) == 'r do notdo o'
    assert scramble(a_tuple) == (13, 12, 5, 32, 2, 54)