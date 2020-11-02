
while True:
    user_selection = input('Please select option 1-3: ')
    try:
        user_selection = int(user_selection)
        break
    except ValueError:
        print("You must enter a number from 1-4")

print("end")
