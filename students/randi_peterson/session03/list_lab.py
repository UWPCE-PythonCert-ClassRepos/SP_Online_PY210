#-----Series 1-----
print('Series 1')
fruitlst = ['Apples','Pears','Oranges','Peaches']
print(fruitlst)

#Add another fruit to end of the list
newfruit = input("Type a fruit name to add to list \n")
fruitlst.append(newfruit)
print(fruitlst)

lstindex = input("Type an index \n")
fruitindex = int(lstindex)-1
print(fruitlst[fruitindex])

#Add another fruit with + to the beginning of the list
newfruit2 = input("Type another fruit name to add to list \n")
newfruit2lst = [newfruit2]
fruitlst = newfruit2lst + fruitlst
print(fruitlst)

#Add another item with .insert() to the beginning of the list
newfruit3 = input("Type yet another fruit name to add to list \n")
fruitlst.insert(0,newfruit3)
print(fruitlst)

#Print all fruits starting with P (case sensitive)
for i in fruitlst:
    if i[0]== 'P':
        print(i)

#-----Series 2-----
print('Series 2')
#Make a copy to protet original fruitlst
fruitlst_s2 = fruitlst[:]
print(fruitlst_s2)

#Remove last item from list
fruitlst_s2.pop()
print(fruitlst_s2)
fruitdelete = input('Name a fruit to delete \n')

for i,item in enumerate(fruitlst_s2):
    if item == fruitdelete:
        fruitlst_s2.pop(i)

print(fruitlst_s2)

#-----Series 3-----
print('Series 3')
#Make a copy to protect original fruitlst
fruitlst_s3 = fruitlst[:]
print(fruitlst_s3)

indices_to_pop = []
#Delete ones you don't like
for i,fruit in enumerate(fruitlst_s3):
    fruit = fruit.lower()
    answer = input('Do you like {}? \n'.format(fruit))
    while answer.lower() != 'yes' and answer.lower() != 'no':
        answer = input('Please answer yes or no! \n')
    if answer.lower() == 'yes':
        pass
    elif answer.lower() == 'no':
        indices_to_pop.append(i)

indices_to_pop.reverse()
for j in indices_to_pop:
    fruitlst_s3.pop(j)
print(fruitlst_s3)


#-----Series 4-----
print('Series 4')
fruitlst_s4 = fruitlst[:]

#Reverse letters in each item
for i,items in enumerate(fruitlst_s4):
    new = items[::-1]
    fruitlst_s4[i] = new

#Remove last item from original
fruitlst.pop()
print(fruitlst)
print(fruitlst_s4)