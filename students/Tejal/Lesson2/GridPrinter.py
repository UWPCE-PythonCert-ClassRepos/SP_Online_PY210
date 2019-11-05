def mlist(size):
    list = []
    for i in range(size):
        list = list + ['+ - '] 
       
    return list

def mmatrix(rows,cols):
    for i in mlist(rows):
        print(i*cols + '+')

