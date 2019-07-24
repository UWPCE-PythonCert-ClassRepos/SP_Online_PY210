import sys
import donor_models as d

# sample data to start with
d1 = d.DonorCollection(d.Donor("Jeff Bezos", [877.33]))
d1.apply_donation("Paul Allen", [100, 10, 800])

def find_donor():
    while True:
        fullname = input("type list to display names or quit to exit to main menu\n" \
                         "Enter full name of donor: ")
        if fullname == "list":
            print(list_names())
        elif fullname != "quit":
            try:
                donation_amount = float(input("Donation amount: "))
                d1.apply_donation(fullname, donation_amount)
            except ValueError:
                print("not a valid response exiting to donor selection")
            d1.donor_list[fullname].send_thankyou()
        else:
            return 

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