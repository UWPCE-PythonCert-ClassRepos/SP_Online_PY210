# windows4life
def series_1():
    print("Let's get rolling with Series 1.")
    print("Here is the original list")
    the_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(the_list, end="\n\n")

    new_fruit = input("I know you want more, what do you want? -> ")
    the_list.append(new_fruit)
    print(the_list, end="\n\n")

    picked_index = int(input("Pick a number of a fruit, Example Apples=1: -> "))
    print(f"You picked {picked_index}: {the_list[picked_index-1]}, nice.", end="\n\n")
    print("I'm going to add Kiwi to the list, as number 1 obviously.")
    the_list = ["Kiwi"] + the_list
    print(the_list, end="\n\n")

    print("Actually, even better is Dragonfruit, sorry for the confusion.")
    the_list.insert(0, "Dragonfruit")
    print(the_list, end="\n\n")

    print("In this list exists those special fruits that start with P:")
    for fruit in the_list:
        if fruit[0] == "P" or fruit[0] == "p":
            print(f"    {fruit}")
    print("End of Series 1", end="\n\n")
    return the_list


def series_2(the_list):
    print("This is Series 2, get pumped.")
    print(the_list, end="\n\n")

    print("I changed my mind, I didn't want your opinion.")
    the_list.pop()
    print(the_list, end="\n\n")
    fruit_to_delete = None

    print("Moar Fruit!!!")
    the_list = the_list * 2
    print(the_list, end="\n\n")
    while fruit_to_delete not in the_list:
        fruit_to_delete = input(
            "Please pick a fruit inside this list you want to remove: -> "
        )
    while fruit_to_delete in the_list:
        the_list.remove(fruit_to_delete)
    print(the_list, end="\n\n")


def series_3(the_list):
    print("Almsot there, this is Series 3!")
    for fruit in the_list[:]:
        liked_response = None
        while liked_response not in ["yes", "y", "no", "n"]:
            liked_response_raw = input(f"Do you like {fruit.lower()}? yes or no: -> ")
            liked_response = liked_response_raw.lower()
        if liked_response in ["no", "n"]:
            the_list.remove(fruit)
    print("\nI guess this is what you like...hmmm, picky much?")
    print(the_list, end="\n\n")


def series_4(the_list):
    print(
        """Alright, lets do this one last time. My name is Series 4,
         and for 2mins I've been the one and only series being worked on."""
    )
    bassackwards_list = []
    for item in the_list:
        bassackwards_list.append(item[::-1])
    bassackwards_list.pop()
    print("Here is the Series 1 Result: ")
    print(the_list, end="\n\n")
    print("Here is the final result, I hope you are happy.")
    print(bassackwards_list, end="\n\n")


def main():
    series1_result = series_1()

    # Use full slice to create copies for each subsequent series
    series_2(series1_result[:])
    series_3(series1_result[:])
    series_4(series1_result[:])


if __name__ == "__main__":

    def response_generator(seq):
        for item in seq:
            yield item

    def input(prompt):  # Mocks input function
        print(prompt, end="")
        response = mocked_resp_gen.__next__()
        print(response)
        return response

    mocked_responses = [
        "UserFruit",
        "3",
        "notinlist",
        "Pears",
        "stubbornNo",
        "Yes",
        "YES",
        "NO",
        "N",
        "y",
        "y",
        "n",
    ]
    mocked_resp_gen = response_generator(mocked_responses)

main()
