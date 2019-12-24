#Donor dict
donor_list=[["Ahmed",123,456,789],
["Sally", 10,11],
["Bob", 12],
["Vladamir", 13.14,1516.17],
["Santa", 181920.21,22,23.24],
]

#send thanks funct
def send_thanks():
    while True:
        query=input("Please enter a Full Name, enter 'list' to see a list of current donors or type quit to exit: ")
        for i in range(0,len(donor_list)):
            if query in donor_list[i][0]:
                new_donate=float(input("How much would you like to donate: \n"))
                donor_list[i].append(new_donate)
                return print(f"\nThank you {query} for your donation of ${new_donate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                    "Sincearly,\n\n"
                    "A low paid intern\n")
                
            elif query=="list":
                    print(donor_list[i][0])
            elif query.lower()=="quit":
                return
            elif query not in donor_list[i][0]:
                new_donate=float(input("\nHow much would you like to donate: \n"))
                donor_list.append([str(query),new_donate])
                return print(f"\nThank you {query} for your donation of ${new_donate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                    "Sincearly,\n\n"
                    "A low paid intern\n")
            
                


#making a sorted list
def sorting_function(dlist):
    sorted_list=[]
    for i in range(0,len(dlist)):
        sorted_list.append([dlist[i][0],sum(dlist[i][1:len(dlist[i])]),len(dlist[i][1:len(dlist[i])]),sum(dlist[i][1:len(dlist[i])])/len(dlist[i][1:len(dlist[i])])])
    return sorted(sorted_list, key=lambda sorted_list:sorted_list[1], reverse=True)
#creating a report
def create_report(): 
    listy=sorting_function(donor_list)
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0,len(listy)):
        print(f"{listy[i][0]:<21} ${listy[i][1]:>12.2f}{listy[i][2]:>11}  ${listy[i][3]:>12.2f}")

#Script
if __name__ == '__main__':
    while True:
        prompt=input(
            "What would you like to do?:\n"
            "A - Send a Thank you\n"
            "B - Create a report\n"
            "C - Quit\n")
        if prompt=="A":
            send_thanks()
        elif prompt=="B":
            create_report()        
        elif prompt=="C":
            break
        else:
            print("\nPlease enter A, B, or C\n")


