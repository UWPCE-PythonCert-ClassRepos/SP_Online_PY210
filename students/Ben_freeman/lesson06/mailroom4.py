import sys
import os
#Donor dict
donor_list={
"Ahmed":[123,456,789],
"Sally": [10,11],
"Bob": [12],
"Vladamir": [13.14,1516.17],
"Santa": [181920.21,22,23.24],
}
def send_thanks_print(query, new_donate):
    print(f"\nThank you {query} for your donation of ${new_donate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                        "Sincearly,\n\n"
                        "A low paid intern\n")
def send_thanks_list():
    print('\n'.join(donor_list))
def send_thanks_add_donor(query,new_donate):
    donor_list[query].append(new_donate)
def send_thanks_update_donor(query, new_donate):
    donor_list[query]=[new_donate]
#send thanks funct
def send_thanks(query="empty_1",new_donate="empty_2"):
    while True:
        if query== "empty_1":
            query=input("Please enter a Full Name, enter 'list' to see a list of current donors, or quit to exit: ")
        if query=="list":
            send_thanks_list()
            break
        elif query.lower()=="quit":
            break
        else:
            if new_donate=="empty_2":
                while True:
                    try:
                        new_donate=float(input("\nHow much would you like to donate: \n"))
                        break
                    except ValueError:
                        print("\nPlease enter a number in numerical form\n")
            else:
                if query in donor_list:
                    send_thanks_add_donor(query,new_donate)
                else:
                    send_thanks_update_donor(query, new_donate)
                return send_thanks_print(query, new_donate)
                break
                

#making a sortable list
def sorting_function(dictionary):
    temp_list=[]
    for keys, values in dictionary.items():
        temp_list.append([sum(values),keys,len(values),sum(values)/len(values)])
    return sorted(temp_list, reverse=True)

#creating a report
def create_report(dictionary=donor_list): 
    listy=sorting_function(dictionary)
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0,len(listy)):
        print(f"{listy[i][1]:<21} ${listy[i][0]:>12.2f}{listy[i][2]:>11}  ${listy[i][3]:>12.2f}")

#writing thank you to all donors function
def mass_send_thanks_text(donor,dictionary):
    return (f"\nThank you {donor} for your donation of ${sum(dictionary[donor]):.2f}, your donations make the work of the 'American society for taking donations' possible.\n\n"
        "Sincearly,\n\n"
        "A low paid intern\n")

def mass_send_thanks(dictionary=donor_list):
    try:
        os.mkdir("Letters")
    except:
        pass
    for donor in dictionary:
        with open(f"Letters/{donor}.txt","w+") as letter:
            letter.write(mass_send_thanks_text(donor,dictionary))
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


