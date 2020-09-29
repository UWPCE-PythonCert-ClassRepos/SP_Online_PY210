


def task_2(seq):
    l = len(seq)-1
    x= []
    for i in seq[1::]:
        n = format(i,'e')
        x.append(n)
    file_name = []
    temp_list = str(seq[0])
    if len(temp_list) == 1:
        file_name = "00" + str(seq[0])
    elif len(temp_list) == 2:
        file_name = "0"+str(seq[0])
    else:
        file_name = seq[0]
    #xSeq = ", ".join([f"{x}"]*l)
    #print(f"file_ {file_name}: +{xSeq}")
    print((f"file_{file_name}: " + ", ".join([f"{x}"])))

seq = (20, 123.4567, 10000, 12345.67)
task_2(seq)
