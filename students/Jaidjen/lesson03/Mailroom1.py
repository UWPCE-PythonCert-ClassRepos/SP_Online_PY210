import sys  # imports go at the top of the file


Mail  =[('James Smith',[2000.25, 500, 27.50]),
        ('Dorothy Parker',[3175, 475.45, 92.30]),
        ('Dohgyu Hwang',[10670, 350.19,175]),
        ('Sally Yu', [100, 925]),
        ('Jenny Ramos',[25.14])]

prompt = "\n".join(("Functions:",
          "Please choose from below options:",
          "1 - Send a Thank You email",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))


def view_mail(Mail):
    print("{:20s}{:20s}{:20s}{:20s}".format("DONOR ", "| TOTAL GIVEN ", "| NUMBER OF GIFTS ", "| AVERAGE GIFTS "))
    print("-----------------------------------------------------------------------------")

    for i in range(len(Mail)):
        donate=[]
        dnr_ave= sum(Mail[i][1])
        ave_amt= int(len(Mail[i][1]))
        tot_ave= dnr_ave/ave_amt
        donate.append(dnr_ave)
        sorted(donate)
        print("{:20s}{:^20.2f}{:^19d}{:^18.2f}".format(Mail[i][0], dnr_ave, len(Mail[i][1]), tot_ave))

def add_mail():
    print("If you want a list of donors please type 'list' ")
    new_mail = input("Please enter the full name of the donor? ")
    for i in range(len(Mail)):
         if new_mail == 'list':
             print("{:<20s}".format(Mail[i][0]))
         elif new_mail == Mail[0]:
            return Mail([0])
            dnr_amt = input("Please enter the donation amount: ")
            print('Thank you', {new_mail}, 'for donating', {dnr_amt})
         else:
             dnr_amt = input("Please enter the donation amount: ")
             Mail.append(new_mail)
             Mail.append(dnr_amt)
             print('Dear',new_mail,',')
             print('Thank you', new_mail,'for donating','{:.2f}'.format(int(dnr_amt)))
             print('We appreciate your generosity.')
             print( )
             print('Sincerely, Donation Team')
             break


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            add_mail()
        elif response == "2":
            view_mail(Mail)
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()