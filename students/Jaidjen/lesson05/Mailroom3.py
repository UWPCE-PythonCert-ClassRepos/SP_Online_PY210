import sys  # imports go at the top of the file


Mail = {1:{'Name':'James Smith', 'Donation':[2000.25,500,27.50]},
              2:{'Name': 'Dorothy Parker','Donation':[3175,475.45,92.30]},
              3:{'Name':'Dohgyu Hwang','Donation':[10670,350.19,175]},
              4:{'Name': 'Sally Yu', 'Donation':[100,925]},
              5:{'Name':'Jenny Ramos','Donation':[25.14]}}

prompt = "\n".join(("Functions:",
          "Please choose from below options:",
          "1 - Send a Thank You to a single donor",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit",
          ">>> "))


def view_mail(Mail):
    print("{:20s}{:20s}{:20s}{:20s}".format("DONOR ", "| TOTAL GIVEN ", "| NUMBER OF GIFTS ", "| AVERAGE GIFTS "))
    print("-----------------------------------------------------------------------------")
    for mail in Mail:
        print("{:20s}{:^20.2f}{:^19d}{:^18.2f}".format(Mail[mail]['Name'],sum(Mail[mail]['Donation']), len(Mail[mail]['Donation']),(sum(Mail[mail]['Donation'])/(len(Mail[mail]['Donation'])))))


def add_mail():
    print("If you want a list of donors please type 'list' ")
    new_mail = input("Please enter the full name of the donor? ")
    if new_mail == 'list':
        print("{:<20s}".format(Mail[Name]))
    else:
        try:
            new_mail == Mail[1]
            dnr_amt = input("Please enter the donation amount: ")
        except ValueError:
            print('Not acceptable')
            raise ValueError
        else:
            Mail['Name']=new_mail
            Mail['Donation']=dnr_amt
            print('Dear',new_mail,',')
            print('Thank you', new_mail,'for donating','{:.2f}'.format(int(dnr_amt)))
            print('We appreciate your generosity.')
            print('Sincerely, Donation Team')


def thankyou_mail():
    for mail in Mail:
        print('Dear',(Mail[mail]['Name']),',')
        print('Thank you for your very kind donation of','{:.2f}'.format(sum(Mail[mail]['Donation'])))
        print('It will be put to very good use.')
        print('Sincerely, Donation Team')



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
            thankyou_mail()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()