def ThankYou(donorlst):
    fullname = input('What is the full name of the donor? Type list to see donors. Type exit to quit task \n')
    if fullname.lower() == 'list':
        for donor in donorlst:
            print(donor[0])
    elif fullname.lower() == "exit":
        return None
    else:
        #Find where donor is in list or create a new one
        donorindex = None
        for index,donors in enumerate(donorlst):
            if donors[0] == fullname:
                donorindex = index
                break
        if donorindex == None:
            donorindex = len(donorlst)
            new_entry = [fullname]
            donorlst.append(new_entry)
        newdonation = float(input('What is the value of the donation (numbers only)?\n'))
        donorlst[donorindex].append(newdonation)

        #Print the thank you email
        print(f'Dear {fullname}, \n Thank you for your generous donation. We appreciate the support from people like you. \n Thank you,\n Charity Name')

def CreateReport(donorslist):
    # Create report data from donor list
    j = 0
    donor_report = []
    for donor in donorlst:
        name = donorlst[j][0]
        donations = len(donorlst[j]) - 1
        total_given = 0
        # Add up all donations
        k = 1
        while k < donations + 1:
            total_given += donorlst[j][k]
            k += 1
        avg_gift = total_given / donations
        donor_report.append([name, total_given, donations, avg_gift])
        j += 1

    # Format report
    header = ['Name', 'Total Given', '# of Gifts', 'Average Gift']
    header_format = "{:<20}" + "{:^15}" + "{:^15}" + "{:^10}"
    row_format = "{:<20}" + "${:>15.2f}" + "{:^15}" + "${:>10.2f}"
    i = 0
    print(header_format.format(*header))
    print('-' * 70)
    for donors in donor_report:
        print(row_format.format(*donor_report[i]))
        i += 1

if __name__ == "__main__":

    #Donors
    donorlst = [['Luke Skywalker', 100, 200, 300], ['Leslie Knope', 100], ['Dwight Schrute',345,35435], ['Freddie Mercury',32432,34], ['Jennifer Aniston', 324,543]]

    #MAIN
    while (True):
        print("Options: \n 1 - Send a Thank You \n 2 - Create Report \n 3 - Exit ")
        response = input('What would you like to do?\n')

        #Send a Thank You
        if response == '1':
            ThankYou(donorlst)

        #Create Report
        elif response == '2':
           CreateReport(donorlst)

        #Exit Program
        elif response =='3':
            break

        #Require valid input
        else:
            print("Please pick a valid option")
