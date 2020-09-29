import sys
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

        if query=="list":
            print('\n'.join(donor_list))
        elif query.lower()=="quit":
            return
        else:
            while True:
                try:
                    new_donate=float(input("\nHow much would you like to donate: \n"))
                    break
                except ValueError:
                    print("\nPlease enter a number in numerical form\n")
            if query in donor_list:
                donor_list[query].append(new_donate)
            else:
                donor_list[query]=[new_donate]
            print(f"\nThank you {query} for your donation of ${new_donate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                "Sincearly,\n\n"
                "A low paid intern\n")
            break

#making a sortable list
def sorting_function(dictionary):
    temp_list=[]
    for keys, values in dictionary.items():
        temp_list.append([sum(values),keys,len(values),sum(values)/len(values)])
    return sorted(temp_list, reverse=True)
#creating a report
def create_report(): 
    listy=sorting_function(donor_list)
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0,len(listy)):
        print(f"{listy[i][1]:<21} ${listy[i][0]:>12.2f}{listy[i][2]:>11}  ${listy[i][3]:>12.2f}")

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
"C":mass_send_thanks,
"D":sys.exit
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
        try:
            menu[prompt.upper()]()
        except KeyError:
            print("\nPlease enter A, B, C or D\n")


