# taskone
# txt = 'file_00{} :   \t{}, {}, {}'.format( 2, round(123.4567, 2), "{:.2e}".format(10000), "{:.2e}".format(12345.67))
# print(txt)


# #tasktwo
# item1 = 2
# item2 = round(123.4567, 2)
# item3 = "{:.2e}".format(10000)
# item4 = "{:.2e}".format(12345.67)
# print(f"file_00{item1} : \t{item2}, {item3}, {item4}")


# #taskthree
# def format_sequence(seq):
#     return "file_{:03d} :\t{:.2f}, {:.2e}, {:.2e}".format(*seq)

# print(format_sequence((2, 123.4567, 10000, 12345.67)))

# #taskfour
# def taskfour(seq):
#     return "{3:02d}, {4}, {2}, {0:02d}, {1}".format(*seq)

# print(taskfour(( 4, 30, 2017, 2, 27)))

#taskfive
# list_1 = ['oranges', 1.3, 'lemons', 1.1]
# print(f"The weight of an {list_1[0].upper()} is {list_1[1]*1.2} and the weight of a {list_1[2].upper()} is {list_1[3]*1.2}")

#tasksix
# print('{:}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))
# print('{:^10d}{:^10d}{:^10d}'.format('Name', 'Age', 'Cost'))
# print('{:10}{:10}{:^10d}'.format('Altaf Lakhi', '24', 1500))

""""
from tabulate import tabulate
data = [['Altaf Lakhi', 24, 1500], ['Huda Quanungo', 9, 200]]
data_1 = tabulate(data, headers=['Name','Age','Cost'])
print(data_1)
"""
# # data
# data_denovo = list()
# data_denovo.append(('Name', 'age', 'cost'))
# data_denovo.append(('Altaf Lakhi', 24, 1400))
# data_denovo.append(('Huda Quanungo', 20000, 200))
# data_denovo.append(('Fahima Lakhi', 100, 200000))
# data_denovo.append(('Aadil', 55, 342))
# # print(data_denovo)
#
# # row formatting
# row = "{name:<14} {age:<5} {cost:<3}".format

# for i in data_denovo:
#     print(row(name = i[0], age=i[1], cost=i[2]))


conseq = (1,2,3,4,5,6,7,8,9,10)
for i in conseq:
    print(