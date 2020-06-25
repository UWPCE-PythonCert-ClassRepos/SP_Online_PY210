#!/usr/bin/env python3

# data structure = list

donor_db = [('Bob', [5, 10, 20]), ('Kathy', [20]),
            ('Sherry', [50, 100]), ('Sophia', [1000]),
            ('Chet', [10000, 10000])]

prompt = "\n".join("Donation Database Menu",
                   "Please choose from below options:",
                   "1 - Send a Thank You",
                   "2 - Create a Report",
                   "3 - Quit",
                   ">>> ")

def exit_program():
    print("Quitting...")
    sys.exit()

def main():
    while True:
        response = input(prompt)

        if response == "1":
            exit_program()
        elif response == "2":
            exit_program()
        elif response == "3":
            exit_program()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()