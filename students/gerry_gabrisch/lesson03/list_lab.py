#!/usr/bin/env python3

###                 Series 1   

fruits = ['Apples','Pears', 'Oranges', 'Peaches']
#print the list...
print('Your list is :', fruits)
#get user input for a fruit to add to the list...
response = input("Please add another fruit to the fruits list now > ")
#make sure the response is consistent with the list and capitalize it...
fruits.append(response.capitalize())
#get input for a postion to display the fruit at that position...
response = input("Enter a number to display the fruit at that postion > ")
#lists index at 0 but people do not think this way, so subtract 1 from their answer...
print(fruits[int(response)-1])
#get input to add a fruit at the beginning of the list...capitalize it too...
response = input("Please add another fruit to the beginning of the fruits list now > ")
response = [response.capitalize()]
#had to use + so add the lists but put the new addition first and add the lists.
#call the new list fruits
fruits = response + fruits
#same as above but with an instert statement...
response = input("Please add another fruit to the beginning of the fruits list now > ")
fruits.insert(0, response.capitalize())

print('Displaying all items that begin with P:')
for item in fruits:
    if item[0] =='P':
        print(item)
        
###                 Series2
        
def delete_fruit(inlist):
    '''prompts the user for a fruit,  if the fruit is in the list then remove that fruit.
    Some users may or may not capitalize so just capitalize the response'''
    #get users fruit to remove...
    response = input("Enter a fruit to have it removed from the list > ").capitalize()
    #if that fruit is in the list then remove that fruit...
    if response in inlist:
        for i in inlist:
            if i == response:
                inlist.remove(response)
        print(response, ' was removed from the list.')
    else:
        #For users that asked for a removal that is not in the list
        #have them try again...
        print(response, ' is not in the fruit list...try again')
        delete_fruit(inlist)
                
        
print(fruits)
fruits.pop()
print('with the last item removed :',fruits)
#Delete fruits from user input...
delete_fruit(fruits)
print('the list with your fruits removed :', fruits)

####                 Series 3

#Create a list to hold all the fruits the user does not like...
nolist = []
#iterate the fruits list, and ask user if they like or do not like that fruit...
#Some users might enter Yes or No so turn the answer to lower case...
for item in fruits:
    response = input("Do you like " + item.lower()+ "? > ")
    #add the no fruits to the list of no fruits...
    if response == 'no':
        nolist.append(item)
    #pass if they like that fruit...
    elif response == 'yes':
        pass
    #handle odd answeres by prompting the user again...
    else:
        print('Invalid answer, please answer yes or no...')
        response =input("Do you like " + item.lower()+ "? > ")
#Cast the lists to sets to easily remove the no like list items from the fruits list...
#then turn the resulting set back to list...
newfruits = list(set(fruits) - set(nolist))
print('the list with the fruits you do not like removed :', newfruits)

###                 Series 4
#reuse the reverse string function from the slicing lab...
def reverse_seq(seq):
    '''reverses a sequence by slicing'''
    #Get the length of the squence...
    positions = len(seq)-1
    #make empty string to hold the reversal...
    reversed = ''
    #go through backwards and concantonate the elements in reverse...
    while positions >=0:
        reversed = reversed + seq[positions]
        positions -= 1
    return reversed
#Create an empty list to hold the revered strings... 
reversed = []
#iterate fruits, reverse the order of the elements, append to a new list..
for item in fruits:
    reversed.append(reverse_seq(item))
#assignemnt says to remove the last item of the origianl list...
fruits = fruits[:-1]
#print as required...
print('fruits with the last item removed :', fruits)
print('reversed fruit names :', reversed)
    
      
    
