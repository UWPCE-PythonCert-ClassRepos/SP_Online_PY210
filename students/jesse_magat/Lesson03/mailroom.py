
donors = [
    ["Michael Jordan", 500.00, 1, 500.00],
    ["Jeff Bezos", 877.33, 1, 877.33],
    ["Bill Gates", 653784.49, 2, 326892.24],
    ["Mark Zuckerberg", 16396.10, 3, 5465.37],
    ["Paul Allen", 708.42, 3, 236.14]
]



def menu():
    return input(
        "\nSelect an option number:"
        "\n1. Send a Thank You"
        "\n2. Create a Report"
        "\n3. Quit\n"
    )


def donors:
for i in donors:
    print(i[0])
	
	
def add_donor:
	
	
	user_add_fruit2 = input("please select another fruit name: ")
#added list to avoid this error "can only concatenate str (not "list") to str"
#converted the input to a list
user_add_fruit2_a = user_add_fruit2.capitalize()
user_new_fruit = [user_add_fruit2_a] #use brackets to get list result

#put second new item in the front
new_list = user_new_fruit + fruit_list
fruit_list = new_list
print(fruit_list)