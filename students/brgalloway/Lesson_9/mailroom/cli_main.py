import sys
import donor_models as d

# donor = d.Donor()
# database = d.DonorCollection()
# form some starting dating 
d1 = d.DonorCollection(d.Donor("Jeff Bezos", [877.33]))

# TODO add another function to create new donors from user input

# Take the 5 donors and put them into a collection
def find_donor():
    while True:
        fullname = input("type list to display names or quit to exit to main menu\n" \
                         "Enter full name of donor: ")
        if fullname == "list":
            output = list_names()
            return print(output)
        elif fullname:
            try:
                donation_amount = float(input("Donation amount: "))
                d1.apply_donation = (fullname, donation_amount)
            except ValueError:
                print("not a valid response exiting to donor selection")
            d2 = d.Donor(fullname, donation_amount)
            d1.donor_list[fullname].apply_donation(donation_amount)
            print(d2.send_thankyou())
        elif fullname == "quit":
            return menu_selection(main_menu, main_dispatch) 

def list_names():
    donor_names = [k for k in sorted(d1.donor_list.keys())]
    return "\n".join(donor_names)

def quit_app():
    return "quit"

# menu prompt and options to select from
prompt = "Choose one of the following options. \n\n" \
    "1 - Send a Thank You to a single donor \n" \
    "2 - Create a Report \n" \
    "3 - Send letters to all donors \n" \
    "4 - Quit \n" \
    ">> "

# value returned from choice keys
main_dispatch = {
    "1": find_donor,
    "2": d1.generate_report,
    "3": d1.bulk_thankyou,
    "4": quit_app
}
    
def menu_selection(prompt, main_dispatch):
    
    while True:
        response = input(prompt)
        response = response.lower()
        response = response.strip()
        try:
            if main_dispatch[response]() == "quit":
                sys.exit()
        except KeyError:
            print("\n\ninvalid response\n")

if __name__ == '__main__':
    menu_selection(prompt, main_dispatch)