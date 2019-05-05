def exchange_first_last(seq):
    """
    :param seq: any python seq, like String,List,Tuple
    :return:
    """
    first = seq[0]
    last = seq[-1]
    middle = seq[1:-1]
    if type(seq) == str:
        new_seq = last + middle + first
        return new_seq
    elif type(seq) == list:
        middle.insert(0, last)
        middle.append(first)
        return middle

def every_other_item(seq):
    new_list=[]
    new_string = ''
    for i in range(0,len(seq),2):
        new_list.append(seq[i])
    if type(seq) == list:
        return new_list
    elif type(seq) == str:
        return new_string.join(new_list)


def remove_first_four_last_four(seq):
    """
    :param seq: String or a list
    :return: return the seq the first 4 and the last 4 items removed
    """
    if len(seq) >8:
        return seq[4:-4]
    return "Length of your seq is less than 8, Change it and try again"

def remove_first_four_last_four_every_other_item(seq):
    """
    This function will call two other functions
    remove_first_four_last_four(seq) to remove first and last four items
    and every_other_item(seq) to remove every other items from the remaining items in the seq
    :param seq: String or a list
    :return:
    """
    seq = remove_first_four_last_four(seq)
    return(every_other_item(seq))

def reverse(seq):
    return seq[::-1]

def third(seq):
    a = len(seq)//3
    return 'Last third is: {}, first third is: {}, middle third is: {}'.format(seq[-3:],seq[:3],seq[a:-a])


test_string = '123456789ABCDE'
test_list = [1,2,3,4,5,6,7,8,9]

if __name__ == '__main__':
    assert exchange_first_last(test_string) == 'E23456789ABCD1'
    assert every_other_item(test_list) == [1, 3, 5, 7, 9]
    assert remove_first_four_last_four_every_other_item(test_string) == '579'
    assert reverse(test_string) == 'EDCBA987654321'
    assert third(test_list) == 'Last third is: [7, 8, 9], first third is: [1, 2, 3], middle third is: [4, 5, 6]'
    print('PASS')
