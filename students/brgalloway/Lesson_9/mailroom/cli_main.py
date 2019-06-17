import sys
import donor_models as d

# form some starting dating 
d1 = d.Donor("Jeff Bezos")
d2 = d.Donor("Paul Allen")
d3 = d.Donor("William Gates, III")
d4 = d.Donor("Bill Ackman")
d5 = d.Donor("Mark Zuckerberg")
d1.donation_total, d1.times_donated, d1.average_donation = 877.33, 1, 877.33
d2.donation_total, d2.times_donated, d2.average_donation = 708.42, 3, 236.14
d3.donation_total, d3.times_donated, d3.average_donation = 653784.49, 2, 326892.24
d4.donation_total, d4.times_donated, d4.average_donation = 2354.05, 3, 784.68
d5.donation_total, d5.times_donated, d5.average_donation = 16396.10, 3, 5465.37

# TODO add another function to create new donors from user input

# Take the 5 donors and put them into a collection
donor_db = d.DonorCollection()
donor_db.append(d1)
donor_db.append(d2)
donor_db.append(d3)
donor_db.append(d4)
donor_db.append(d5)


def quit_app():
    return "quit"

# menu prompt and options to select from
prompt = "Choose one of the following options. \n\n" \
    "1 - Send a Thank You to a single donor \n" \
    "2 - Create a Report \n" \
    "3 - Send letters to all donors \n" \
    "4 - Quit \n" \
    ">> "

# shortend names for dipatch dictionary
find_donor = d.DonorCollection.find_donor
generate_report = d.DonorCollection.generate_report
bulk_thankyou = d.DonorCollection.bulk_thankyou

# value returned from choice keys
main_dispatch = {
    "1": find_donor,
    "2": generate_report,
    "3": bulk_thankyou,
    "4": quit_app
}
    
def menu_selection(prompt, main_dispatch):
    
    while True:
        response = input(prompt)
        response = response.lower()
        response = response.strip()
        try:
            if response in main_dispatch:
                if response == "1":
                    find_donor(d.DonorCollection, donor_db)
                elif response == "2":
                    generate_report(d.DonorCollection, donor_db)
                elif response == "3":
                    bulk_thankyou(d.DonorCollection, donor_db)
                elif response == "4":
                    sys.exit()
        except KeyError:
            print("\n\ninvalid response\n")

if __name__ == '__main__':
    menu_selection(prompt, main_dispatch)