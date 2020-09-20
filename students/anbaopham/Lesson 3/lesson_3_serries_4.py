
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
l = fruit_list[0:-1]
new_list = []
for i in l:
    new_list.append(i[::-1])

print("old list: ", fruit_list)
print("old list after remove last item: ",l)
print("new list: " , new_list[::-1])
