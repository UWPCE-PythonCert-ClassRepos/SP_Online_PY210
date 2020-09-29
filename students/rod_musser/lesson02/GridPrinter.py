def printGrid(n=9):
    # grid size must be at least 3
    if (n < 3):
        return
    width = height = (n - 1) // 2
    rows = 2
    columns = 2

    for i in range(rows):
        for h in range(height + 2):
            str = ''
            if (h == 0 or (i == rows - 1 and h == height + 1)):
                for j in range(columns):
                    for w in range(width + 1):
                        if (w == 0):
                            str = str + '+ '
                        else:
                            str = str + '- '
                # add last character in the row
                str = str + '+'
            elif (h < height + 1):
                for j in range(columns):
                    for w in range(width + 1):
                        if (w == 0):
                            str = str + '| '
                        else:
                            str = str + '  '
                # add last character in the row
                str = str + '|'
            if (str != ''):
                print(str)


def printGrid2(x, y):
    if (x < 1 or y < 3):
        return
    width = height = y
    rows = x
    columns = x

    for i in range(rows):
        for h in range(height + 2):
            str = ''
            if (h == 0 or (i == rows - 1 and h == height + 1)):
                for j in range(columns):
                    for w in range(width + 1):
                        if (w == 0):
                            str = str + '+ '
                        else:
                            str = str + '- '
                # add last character in the row
                str = str + '+'
            elif (h < height + 1):
                for j in range(columns):
                    for w in range(width + 1):
                        if (w == 0):
                            str = str + '| '
                        else:
                            str = str + '  '
                # add last character in the row
                str = str + '|'
            if (str != ''):
                print(str)

