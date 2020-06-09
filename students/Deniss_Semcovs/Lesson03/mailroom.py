#!/usr/bin/env python3
data = [
    ["Tom Hanks", 1000, 500],
    ["Leonardo DiCaprio", 300, 1200, 500],
    ["Natalie Portman", 5000],
    ["Harrison Ford", 500, 2000, 100],
    ["Scarlett Johansson", 1500, 1000],
    ["Jennifer Aniston", 2000, 2000, 2000],
]
while True:
    print(
"""
To Send a Thank You Note enter "1"
To create a report enter "2"
To quit enter "3":
""")

    resp = int(input("Enter your choice: "))
    while resp == 1:
        print("Print 'list' to view donor names.")
        donName = str(input("Please enter full name of the donor: "))
        if donName == "list":
            for i in data:
                print(i[0])
        else:
            for i in data:
                if donName == i[0]:
                    donation = int(input("Please enter the donation amount: "))
                    i.append(donation)            
                    print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(donName, donation))
                    break
            else:
                newDonation = int(input("This is a new donor, please enter the donation amount: "))
                print("Letter for the donor: ")
                print("Hello {}, thank you for your generous donation of ${} to support our cause.".format(donName, newDonation))
            break
    if resp == 2:
        tags = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        print("{:20s}| {:10s} | {:10s} | {:10s}".format(*tags))
        print(("-")*61)
        for i in data:
            dName = (i[0])
            tGiven = sum(i[1:])
            nGifts = len(i[1:])
            aGift = ((sum(i[1:]))/(len(i[1:])))
            data2 = (dName, tGiven, nGifts, aGift)
            print("{:20s} $ {:10d}   {:10d}  $ {:.2f}".format(*data2))
    if resp == 3:
        break