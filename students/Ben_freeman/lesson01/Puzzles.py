
def missing_char(str, n):
    front = str[:n] 
    back = str[n+1:]
    return front + back

def front_back(str):
    front = str[0]
    middle = str[1:len(str)-1]
    back = str[len(str)-1]
    return back+middle+front