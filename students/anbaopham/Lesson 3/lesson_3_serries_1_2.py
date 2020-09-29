response = input("what fruit will be added? > ")

fruit_id_input = int(input("what's fruit ID?"))

add_fruit_pos0 = input("What's fruit will be added in position 0?")
id_number = fruit_id_input -1
fruit_list = ["Apples", "Pears","Oranges","Peaches"]
fruit_list.append(response)
print(fruit_list)
print(fruit_list[id_number])
add_fruit_pos0 =[add_fruit_pos0,]
add_fruit_pos0_list = add_fruit_pos0 + fruit_list[:]
print("new fruit list after adding new fruit at pos 0:", add_fruit_pos0_list)
fruit_list.insert(0,add_fruit_pos0[0])
print("new list using 'insert':  ", fruit_list)
P_fruit_list = []
for i in fruit_list:
    if i[0] == "P":
        P_fruit_list.append(i)

print("fruit start with 'P': ", P_fruit_list)

dL = fruit_list[:-2]
print(dL)
newList = fruit_list*2
print("double list: ",newList)
#print("length of newList: ", len(newList))

updated_list = []
m = 0

def remove_fruit(deleted_fruit, newList, updated_list):
    n =0
    for i in newList:
        if i == deleted_fruit:
            for j in newList:
                if j != deleted_fruit:
                    updated_list.append(j)
                else:
                    pass
            n = n+1
            break

    return updated_list, n

while m<1:

    if m ==0:
        deleted_fruit = input("What fruit do you want to remove? ")
        if deleted_fruit == "":
            break
        updated_list, n =remove_fruit(deleted_fruit, newList, updated_list)
        m = n
print("this updated_list: ", updated_list)
#print("length of updated_list: ", len(updated_list))
