# Author: Brian Minsk
donor_db = [("Dee Zaster", [10000, 15000]), 
            ("Owen Money", [7000]), 
            ("Shanda Lear", [100, 900, 1500]), 
            ("Joe King", [500, 700, 500]),
            ("Artie Choke", [1600, 1800])]

prompt = "\n".join(("Please choose an option:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

def main():
    while True:
        response = input(prompt)
        if response == 1:
            send_thank_you()
        elif response == 2:
            create_report()
        elif response == 3:
            exit_program()
        else:
            print("Please type '1', '2', or '3' to select one of the available options.")

if __name__ == "__main__":
   main()
