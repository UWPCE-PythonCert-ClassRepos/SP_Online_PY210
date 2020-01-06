import sys  # imports go at the top of the file


donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

prompt = "\n".join(("Welcome to the Mail Room App.",
                    "Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Quit",
                    "to exit from a task and return to the menu, enter 'back'",
                    ">>> "))

prompt2 = "\n".join(("- To send a thank you message to a donor, enter a name.",
                     "- To see a list of current donors, enter 'list'.",">>> "))


def send_thank_you():
    response2 = input(prompt2)
    if response2.strip() == "list":
        print("\nhi\n")
    elif response2.strip() == "back":
        print("\n")
        pass


def create_report():
    print("\nhi\n")


def exit_program():
    print("Exiting...")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()
