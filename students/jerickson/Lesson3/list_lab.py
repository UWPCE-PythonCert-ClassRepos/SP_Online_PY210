# windows4life
def input(*args):  # Mocks input function
    return "3"


def series_1():
    print("Here is the original list")
    the_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(the_list, end="\n\n")
    new_fruit = input("I know you want more, what do you want? -> ")
    the_list.append(new_fruit)
    print(the_list, end="\n\n")
    picked_index = int(input("Pick a number of a fruit, Apples=1: -> "))
    print(f"You picked {the_list[picked_index-1]}, nice.", end="\n\n")
    print("I'm going to add Kiwi to the list, as number 1 obviously.")
    the_list = ["Kiwi"] + the_list
    print(the_list, end="\n\n")
    print("Actually, even better is Dragonfruit, sorry for the confusion.")
    the_list.insert(0, "Dragonfruit")
    print(the_list, end="\n\n")
    print("In this list exists those special fruits that start with P:")
    for fruit in the_list:
        if fruit[0] == "P" or fruit[0] == "p":
            print(fruit)
    return the_list


if __name__ == "__main__":
    series1_result = series_1()
