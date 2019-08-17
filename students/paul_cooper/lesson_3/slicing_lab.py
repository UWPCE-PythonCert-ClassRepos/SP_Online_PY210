s = 'aeronautical'
q = 'Happy Holidays'
tup =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
p = '123456'


def exchange_first_last(x):
    j = list(x)
    y = j[0]
    q = j[-1]
    j[0] = q
    j[-1] = y
    if type(x) == tuple:
        return tuple(j)
    elif type(x) == str:
        j = ''.join(j)
        return(j)

def every_other_item(x):
    y = list(x)
    j = y[::2]
               
    if type(x) == tuple:
        return tuple(j)
    elif type(x) == str:
        j = ''.join(j)
        return(j)

def first4_last4(x):
    y = list(x)
    j = y[4:-4]

    if type(x) == tuple:
        return tuple(j)
    elif type(x) == str:
        j = ''.join(j)
        return(j)

def reversed(x):
    y = list(x)
    j = y[::-1]

    if type(x) == tuple:
        return tuple(j)
    elif type(x) == str:
        j = ''.join(j)
        return(j)

def thirds(x):
    y =list(x)
    q = int(len(y)/3)
    j = y[-q:]+y[:2*q]
    
    if type(x) == tuple:
        return tuple(j)
    elif type(x) == str:
        j = ''.join(j)
        return(j)
        
print(tup)
print(s)
print(exchange_first_last(tup))
print(exchange_first_last(s))
print(every_other_item(tup))
print(every_other_item(s))
print(first4_last4(tup))
print(first4_last4(s))
print(reversed(tup))
print(reversed(s))
print(thirds(tup))
print(thirds(s))
