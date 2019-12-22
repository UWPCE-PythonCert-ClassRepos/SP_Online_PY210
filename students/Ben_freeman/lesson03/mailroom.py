#Donor dict
donorlist={
"Ahmed":[123,456,789],
"Sally": [10,11],
"Bob": [12],
"Vladamir": [13.14,1516.17],
"Santa": [181920.21,22,23.24],
}

#send thanks funct
def sndthx():
    while True:
        qry=input("Please enter a Full Name or enter 'list' to see a list of current donors: ")
        if qry in donorlist:
            Newdonate=float(input("How much would you like to donate: \n"))
            donorlist[qry].append(Newdonate)
            print(f"\nThank you {qry} for your donation of ${Newdonate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                "Sincearly,\n\n"
                "A low paid intern\n")
            break
        elif qry=="list":
            print('\n'.join(donorlist))
        elif qry not in donorlist:
            donorlist[qry]=[]
            Newdonate=float(input("\nHow much would you like to donate: \n"))
            donorlist[qry].append(Newdonate)
            print(f"\nThank you {qry} for your donation of ${Newdonate}, your donations make the work of the 'American society for taking donations' possible.\n\n"
                "Sincearly,\n\n"
                "A low paid intern\n")
            break

#making a sortable list
def sdonor(dlist):
    mrgl={}
    for i in dlist:
        mrgl[i]=[sum(dlist[i]),len(dlist[i]),sum(dlist[i])/len(dlist[i])]
    flist=[]
    for keys, values in mrgl.items():
        values.append(keys)
        flist.append(values)
    return sorted(flist, key=lambda flist:flist[0], reverse=True)
#creating a report
def crtrpt(): 
    listy=sdonor(donorlist)
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}")
    print(f"-------------------------------------------------------------")
    for i in range(0,len(listy)):
        print(f"{listy[i][3]:<21} ${listy[i][0]:>12.2f}{listy[i][1]:>11}  ${listy[i][2]:>12.2f}")

#Script
if __name__ == '__main__':
    while True:
        prompt=input(
            "What would you like to do?:\n"
            "A - Send a Thank you\n"
            "B - Create a report\n"
            "C - Quit\n")
        if prompt=="A":
            sndthx()
        elif prompt=="B":
            crtrpt()        
        elif prompt=="C":
            break
        else:
            print("\nPlease enter A, B, or C\n")


