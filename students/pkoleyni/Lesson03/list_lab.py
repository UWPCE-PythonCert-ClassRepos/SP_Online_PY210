#!/usr/bin/env python3

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

def add_fruit(seq):
    seq.append(input('Enter name of a fruit >'))
    return seq

def find_by_index(seq):
    user_input = input('Enter a number in range of 1 to {} >'.format(len(seq) + 1))
    return ('You have entered {} which is {} from the fruit_list'.format(user_input,seq[int(user_input)-1]) )

def find_by_letter(seq, letter ='P'):
    for item in fruit_list:
        if letter in item:
            return (item)

def search_and_delete(seq):
    item_to_delete = input('Enter an item to be deleted from the list: ')
    while not(item_to_delete in seq):
        item_to_delete = input('Item you entered is not in the list, Enter another item: ')
    for item in seq:
        if item == item_to_delete:
            seq.remove(item)
    return ('{} has been removed from the list'.format(item_to_delete),seq)

def do_you_like_it(seq):
    like_list = []
    for item in seq:
        usr_input = input('Do you like {}: ?'.format(item.lower()))
        while not ('Yes' in usr_input or 'No' in usr_input):
            print('Please enter \'Yes\' or \'No\' ')
            usr_input = input('Do you like {}: ?'.format(item.lower()))
        if usr_input == 'Yes':
            like_list.append(item)
    return like_list



def series_4(seq):
    new_seq = []
    for item in seq:
        new_seq.append(item[::-1])
    del seq[-1]
    return seq,new_seq


if __name__ == '__main__':
    # Series_1
    print(20*'_','Series_1', 20*'_')
    print ('Fruit_list: ',fruit_list)
    print (add_fruit(fruit_list))
    print (find_by_index(fruit_list))
    print ('Adding new fruit: ',['Banana'] + fruit_list)
    fruit_list.insert(0, 'Banana')
    print ('Adding another fruit to the beginning of the list', fruit_list)
    print("Fruits in the list that begin with \"P\":", find_by_letter(fruit_list))
    #Series_2
    print (20*'_', 'Series_2', 20*'_')
    print ('fruit_list: ',fruit_list)
    del fruit_list[-1]
    print ('Last item removed from fruit_list:',fruit_list )
    print ('Doubling the size of the fruit list ...')
    fruit_list = fruit_list * 2
    print ('fruit list times 2', fruit_list)
    print (search_and_delete(fruit_list))
    #Series_3
    print(20*'_', 'Series_3', 20*'_')
    print ('Reverting back fruit list to its original values ')
    fruit_list=[]
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print (fruit_list)
    print('Here is the list of the fruits you like ',do_you_like_it(fruit_list))
    # Series_4
    print(20*'_', 'Series_4', 20*'_')
    print (series_4(fruit_list))


