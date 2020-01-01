#Donor dict
donor_list={
"Ahmed":[123,456,789],
"Sally": [10,11],
"Bob": [12],
"Vladamir": [13.14,1516.17],
"Santa": [181920.21,22,23.24],
}


#send thanks funct
def send_thanks():
    while True:
        query=input("Please enter a Full Name, enter 'list' to see a list of current donors, or quit to exit: ")
        if query in donor_list:
            new_donate=float(input("How much would you like to donate: \n"))
            donor_list[query].append(new_donate)
            print(f"\nThank you {query} for your donation of ${new_donate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                "Sincearly,\n\n"
                "A low paid intern\n")
            break
        elif query=="list":
            print('\n'.join(donor_list))
        elif query.lower()=="quit":
            return
        elif query not in donor_list:
            donor_list[query]=[]
            new_donate=float(input("\nHow much would you like to donate: \n"))
            donor_list[query].append(new_donate)
            print(f"\nThank you {query} for your donation of ${new_donate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                "Sincearly,\n\n"
                "A low paid intern\n")
            break
        

#making a sortable list
def sorting_function(dlist):
    mrgl={}
    for i in dlist:
        mrgl[i]=[sum(dlist[i]),len(dlist[i]),sum(dlist[i])/len(dlist[i])]
    flist=[]
    for keys, values in mrgl.items():
        values.append(keys)
        flist.append(values)
    return sorted(flist, key=lambda flist:flist[0], reverse=True)
#creating a report
def create_report(): 
    listy=sorting_function(donor_list)
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0,len(listy)):
        print(f"{listy[i][3]:<21} ${listy[i][0]:>12.2f}{listy[i][1]:>11}  ${listy[i][2]:>12.2f}")

#writing thank you to all donors function
def mass_send_thanks():
    for donor in donor_list:
        with open(f"{donor}.txt","w+") as letter:
            letter.write(f"\nThank you {donor} for your donation of ${sum(donor_list[donor]):.2f}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                    "Sincearly,\n\n"
                    "A low paid intern\n")
    print("\nSending out thank you letters\n")

#Menu dict
menu={
"A":send_thanks,
"B":create_report,
"C":mass_send_thanks
}

#Script
if __name__ == '__main__':
    while True:
        prompt=input(
            "What would you like to do?:\n"
            "A - Send a thank you\n"
            "B - Create a report\n"
            "C - Send a thank you to all donors\n"
            "D - Quit\n")
        if prompt.upper() in ["A","B","C"]:
            menu[prompt.upper()]()
        elif prompt.upper() == "D":
            break

        else:
            print("\nPlease enter A, B, C or D\n")


