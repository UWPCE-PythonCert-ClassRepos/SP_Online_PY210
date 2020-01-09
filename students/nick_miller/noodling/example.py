import sys  # imports go at the top of the file


fruits = ['Apples', 'Oranges', 'Pears']

prompt = "\n".join(("Welcome to the fruit stand!",
          "Please choose from below options:",
          "1 - View fruits",
          "2 - Add a fruit",
          "3 - Remove a fruit",
          "4 - Exit",
          ">>> "))


def view_fruits():
    print("\n".join(fruits))


def add_fruit():
    new_fruit = input("Name of the fruit to add?").title()
    fruits.append(new_fruit)


def remove_fruit():
    purge_fruit = input("Name of the fruit to remove?").title()
    if purge_fruit not in fruits:
        print("This fruit does not exist!")
    else:
        fruits.remove(purge_fruit)

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            view_fruits()
        elif response == "2":
            add_fruit()
        elif response == "3":
            remove_fruit()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()