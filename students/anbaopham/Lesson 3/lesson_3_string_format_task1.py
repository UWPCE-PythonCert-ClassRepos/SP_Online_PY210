def task_1(seq):
    l = len(seq)-1
    x=[]
    for i in seq[1::]:
        n = format(i,'e')
        x.append(n)
    fileN =[]
    tempL = str(x[0])
    if len(tempL)==1:
        fileN = "00" + str(seq[0])
    elif len(tempL)==2:
        fileN = "0"+str(seq[0])
    else:
        fileN = seq[0]
    
    print(("file_{}: " + ", ".join(["{}"]*l)).format(fileN, *x))

seq = ( 2, 123.4567, 10000, 12345.67)
task_1(seq)
