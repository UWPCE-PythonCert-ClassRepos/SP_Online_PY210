import sys
import donor_models as d


d1 = d.Donor("Jeff Bezos")
d2 = d.Donor("Paul Allen")
d3 = d.Donor("William Gates, III")
d4 = d.Donor("Bill Ackman")
d5 = d.Donor("Mark Zuckerberg")
d1.donation_total, d1.times_donated, d1.average_donation = 877.33, 1, 877.33
d2.donation_total, d2.times_donated, d2.average_donation = 708.42, 3, 236.14
d3.donation_total, d3.times_donated, d3.average_donation = 653784.49, 2, 326892.24
d4.donation_total, d4.times_donated, d4.average_donation = 2354.05, 3, 784.68
d5.donation_total, d5.times_donated, d5.average_donation =16396.10, 3, 5465.37

donor_db = d.DonorCollection()
donor_db.append(d1)
donor_db.append(d2)
donor_db.append(d3)
donor_db.append(d4)
donor_db.append(d5)

print(donor_db.donor_list)
# menu prompt and options to select from
self.prompt = "Choose one of the following options. \n\n" \
    "1 - Send a Thank You to a single donor \n" \
    "2 - Create a Report \n" \
    "3 - Send letters to all donors \n" \
    "4 - Quit \n" \
    ">> "

# value returned from choice keys
# TODO configure options 1-3 as classes
self.main_dispatch = {
    "1": d.find_donor,
    "2": m.generate_report,
    "3": m.bulk_thankyou,
    "4": self.quit_app
}
    
def quit_app(self):
    return "quit"


def menu_selection(self):
    
    while True:
        response = input(self.prompt)
        response = response.lower()
        response = response.strip()
        try:
            if self.main_dispatch[response]() == "quit":
                sys.exit()
        except KeyError:
            print("\n\ninvalid response\n")

if __name__ == '__main__':
    menu_selection()