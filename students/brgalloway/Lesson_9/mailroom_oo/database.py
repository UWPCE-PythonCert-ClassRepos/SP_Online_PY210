from mailroom_oo import donor_models as Donor

donors_list = {
    "Jeff Bezos": {
        "donation_total": 877.33,
        "times_donated": 1,
        "average_donation": 877.33
    },
    "Paul Allen": {
        "donation_total": 708.42,
        "times_donated": 3,
        "average_donation": 236.14
    },
    "William Gates, III": {
        "donation_total": 653784.49,
        "times_donated": 2,
        "average_donation": 326892.24
    },
    "Bill Ackman": {
        "donation_total": 2354.05,
        "times_donated": 3,
        "average_donation": 784.68
    },
    "Mark Zuckerberg": {
        "donation_total": 16396.10,
        "times_donated": 3,
        "average_donation": 5465.37
    }
}

class Database(object):

    # helper function to sort by total
    def sort_donors(a_dict):
        return a_dict[1]["donation_total"]


    def generate_report(donors_list=donors_list):
        '''
        Generate report based on menu choice
        and return user to the menu prompt  
        '''  
        single_report = []
        sorted_list = sorted(donors_list.items(), key=sort_donors, reverse=True)
        print("{:<20}|{:^15}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
        print("-" * 70)

        name = [i[0] for i in sorted_list]
    
        for donors in range(len(name)):  
            total_formatted = [sorted_list[donors][1][i] for i in sorted_list[donors][1]]
            print(f"{name[donors]:<20}${total_formatted[0]:>14.2f}{total_formatted[1]:^18}${total_formatted[2]:>12.2f}")
            
        single_report = f"{name[donors]:<20}${total_formatted[0]:>14.2f}{total_formatted[1]:^18}${total_formatted[2]:>12.2f}"
        
        return single_report


if __name__ == "__main__":
    main()