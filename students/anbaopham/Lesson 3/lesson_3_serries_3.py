
fruit_list = ["Apples", "Pears","Oranges","Peaches"]

updated_list =[]
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
m = 0
while m < 1:
    for i in fruit_list:
        askQ = input("do you love {} ? ".format(i).lower() )
        if len(askQ) == 0:
            print("please try again")
            break


        elif askQ.lower() == "yes" or askQ.lower() == "y":
            print("good")
            pass

        elif askQ.lower() == "no" or askQ.lower() == "n":
            remove_fruit(i,fruit_list,updated_list)
        elif askQ.lower() =="exit" or askQ.lower() == "x":
            m = m+1
            break
        else:
            print("not good")
            break

if m > 0:
    print(updated_list)
