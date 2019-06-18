def print_grid(x, y):
    total_width = x*(y+1)+1
    for i in range(total_width):
        temp = ""
        for j in range(total_width):
            if i % (total_width//x) == 0:
                if j % (total_width//x) == 0:
                    temp += "+ "
                else:
                    temp += "- "
            else:
                if j % (total_width//x) == 0:
                    temp += "| "
                else:
                    temp += "  "
        temp = temp[:-1]
        print(temp)
            



if __name__ == "__main__":
    print_grid(5,5)