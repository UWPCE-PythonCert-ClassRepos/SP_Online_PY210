
fruit_list = ["Apples", "Pears","Oranges","Peaches"]
l = fruit_list[0:-1]
newList = []
for i in l:
    newList.append(i[::-1])

print("old list: ", fruit_list)
print("old list after remove last item: ",l)
print("new list: " ,newList[::-1])
