def print_grid():
    text1 = "+ " + "- "*4 + "+ " + "- "*4 + "+"
    text2 = "| " + "  "*4 + "| " + "  "*4 + "|"

    for j in range(2):
        print(text1)
        for i in range(4):
            print(text2)
    print(text1)

if __name__ == "__main__":
    print_grid()