
def task_5(seq):
    newL = []
    for i in seq:
        for j in i:
            newL.append(len(j))
            l = max(newL)
    space = " "*10
    width = l
    print(l)
    for a,b,c in seq:

        
        print(f'{a:<{width}}{space}{b:^{width}}{space}{c:>{width}}')

seq = [["Name", "Age", "Cost"],["name_1", "1", "$2"],["name_2", "2", "$20"],
["name_3", "3", "$200"],["name_4", "4", "$2000"]]
task_5(seq)
