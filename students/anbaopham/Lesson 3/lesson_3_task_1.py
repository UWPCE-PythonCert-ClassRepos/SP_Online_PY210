def exchange_first_last(seq):

    a_new_squence = list(seq)
    tempS = a_new_squence[0]
    a_new_squence[0] = a_new_squence[-1]
    a_new_squence[-1] = tempS
    if isinstance(seq,str):
        a_new_squence ="".join(a_new_squence)

    return a_new_squence


def remove_one(seq):
    l = list(seq)
    newList =[]
    newList = l[0:len(l):2]
    if isinstance(seq,str):
        newList ="".join(newList)

    return newList

def remove_one_4(seq):
    l = list(seq)

    tempList = l[4:len(l)-4]

    if isinstance(seq,str):
        tempList ="".join(tempList)

    return remove_one(tempList)

def sliceReversed(seq):
    l = list(seq)
    tempList = l[::-1]
    if isinstance(seq,str):
        tempList ="".join(tempList)
    return tempList

def reOrder(seq):
    l = list(seq)
    tempList = l[len(l)-3:len(l)] + l[0:3] + l[3:len(l)-3]

    if isinstance(seq,str):
        tempList="".join(tempList)
    return tempList

if __name__ == "__main__":

    a_string = "this is a string"
    a_tuple = (2,54,13,12,5,32)

    a_string_1 = "this is a string1234"
    a_tuple_1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == [32,54,13,12,5,2]

    assert remove_one(a_string_1) == "ti sasrn13"
    assert remove_one(a_tuple_1) == [1,3,5,7,9,11,13,15]

    assert remove_one_4(a_string_1) == " sasrn"
    assert remove_one_4(a_tuple_1) ==[5,7,9,11]

    assert sliceReversed(a_tuple) == [32,5,12,13,54,2]

    assert reOrder(a_tuple_1) == [13,14,15,1,2,3,4,5,6,7,8,9,10,11,12]

    print("good")
