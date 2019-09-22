#Grid Printer

for i in range(11):
    if i == 0 or i == 5 or i == 10:
        print('+' + ('-' * 4) + '+' + ('-' * 4) + '+')
    else:
        print("|" + '    ' + "|" + '    ' + '|')

