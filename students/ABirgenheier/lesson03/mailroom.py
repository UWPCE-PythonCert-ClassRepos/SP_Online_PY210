database = [
    ["Mike", 3, 200, 150, 50],
    ["Tony", 3, 150, 50, 250],
    ["Sarah", 3, 150, 150, 150]
]


def menu():
    user_input = input(
        "Please select from following options: (s) to select donar, (c) to create report, or (q) to quit program:   ")
    while user_input != 'q' or user_input != 'Q':
        if user_input == 's' or user_input == 'S':
            sendReport()
        elif user_input == 'c' or user_input == 'C':
            createReport()
        else:
            print("Unknown command.. try again!  ")

        user_input = input(
            "Please select from following options: (s) to select donar, (c) to create report, or (q) to quit program:   ")


def sendReport():
    user_input = input(
        "Would you like to (a) add a donar, (s) select a donor, (sa) select all donars , or (q) to quit:   ")
    options = {
        "a": addDonar,
        "s": selectDonar,
        "sa": selectAllDonar
    }
    while user_input != "q":
        if user_input in options:
            selected_function = options[user_input]
            selected_function()


def addDonar():
    _name = input("Please insert name of donar:   ")
    i = 1
    _donations = []
    while i < 4:
        _donation = int(input("Please insert amount donated by {name} for their donation number {number}:  ".format(
            name=_name, number=i)))
        _donations.append(_donation)
        i += 1
    print("Added {name} and their 3 donations of a sum of ${sum}".format(
        name=_name, sum=sum((_donations))))
    database.append("[{name}, 3".format(
        name=_name))
    database.extend(_donations)
    print(database)
    menu()


def selectDonar():
    _name = input("Please insert name of donar you would like to view:   ")
    i = 0
    while i < len(database):
        if _name == database[i][0]:
            _message = input(
                "Please insert the message you would like to send to {name}:   ".format(name=_name))
            print("""You wrote.....
            Dear {name},
            {message} """.format(name=_name, message=_message))
            menu()
        i += 1
    print("Im sorry, I do not believe we have a record of {name} in our system. Try again.".format(
        name=_name))
    selectDonar()


def selectAllDonar():
    i = 0
    while i < len(database):
        _donars = database[i][0]
        print(_donars)
        i += 1
    _message = input(
        "Please insert the message you would like to send the donars above:  ")
    print("Message:  {sent}".format(sent=_message))
    print("Sent!")

    menu()


def createReport():
    row = "| {name:<10s} | {num:17d} | {n1:14d} | {n2:13d} | {n3:13d} |".format
    for p in database:
        print(
            "|   Name     |   No Donations    |   Donation 1   |  Donation 2   |  Donation 3   |")
        print(row(name=p[0], num=p[1], n1=p[2], n2=p[3],  n3=p[4]))
        menu()


menu()
