# tuple1 = (2, 123.4567, 10000, 12345.67)
# print('file_{:03d} :   {:.2f}, {:.2e}, {:.3e}'.format(*tuple1))
#
# print("file_{:03d} : {:8.2f}, {:.2e}, {:.3e}".format(2, 123.4567, 10000, 12345.67))
#
#
# name = ("Abracatabra","Jo", "Dave")
# age = (3, 28, 100)
# cost = (29.95, 80, 1950345.678)
# l = len(name)
#
# format = ('{:^20}'* l).format(*name) # Align the name in the middle
# format2 = ('{:^20}'* l).format(*age)  # Align the age in the middle
# format3 = ('{:^20.2f}'* l).format(*cost) # Align the price in the middle
# print ("Task 6\n")
# print (format)
# print (format2)
# print (format3)

# forTable = (["Henry", 5, 300], ["River", 0.2, 6000], ["Alicia", 35, 200], ["Daddio", 36, 8000])
#
# key = ["name", "age", "cost"]
# row1 = forTable[0]
# row2 = forTable[1]
# row3 = forTable[2]
# row4 = forTable[3]
#
# print(f"{key[0]:<8}{key[1]:<8}{key[2]:<8}")
# print(f"{row1[0]:<8}{row1[1]:<8}{row1[2]:<8}")
# print(f"{row2[0]:<8}{row2[1]:<8}{row2[2]:<8}")
# print(f"{row3[0]:<8}{row3[1]:<8}{row3[2]:<8}")
# print(f"{row4[0]:<8}{row4[1]:<8}{row4[2]:<8}")

tuplex = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

str({tuplex[0:5]):^5})

print(str({tuplex[0:5]:^5}))
