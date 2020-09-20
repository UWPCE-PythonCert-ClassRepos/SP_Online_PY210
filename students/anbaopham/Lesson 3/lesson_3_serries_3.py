
fruit_list = ["Apples", "Pears","Oranges","Peaches"]

updated_list = []
def remove_fruit(deleted_fruit, newList, updated_list):
    n =0
    for i in newList:
        if i == deleted_fruit:
            for j in newList:
                if j != deleted_fruit:
                    updated_list.append(j)
                else:
                    pass
            n = n + 1
            break
    return updated_list, n
m = 0
while m < 1:
    for i in fruit_list:
        ask_question = input("do you love {} ? ".format(i).lower() )
        if len(ask_question) == 0:
            print("please try again")
            break


        elif ask_question.lower() == "yes" or ask_question.lower() == "y":
            print("good")
            pass

        elif ask_question.lower() == "no" or ask_question.lower() == "n":
            remove_fruit(i,fruit_list,updated_list)
        elif ask_question.lower() =="exit" or ask_question.lower() == "x":
            m = m+1
            break
        else:
            print("not good")
            break

if m > 0:
    print(updated_list)
