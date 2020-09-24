
def formatter(in_tuple):
    l = len(in_tuple)
    form_string = "{:d}"
    #print(("file_{}: " + ", ".join(["{}"]*l)).format(fileN, *x))
    print(f"the {l} numbers are: " + ", ".join(["{}"]*l).format(*in_tuple))



in_tuple = (1, 3, 5, 7, 8)
formatter(in_tuple)
