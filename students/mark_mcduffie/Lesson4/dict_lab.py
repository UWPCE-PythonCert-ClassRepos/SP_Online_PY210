#Mark McDuffie
#Dictionaries Lab
#3/26/20

#Dictionaries1
def dic1():
    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(d)
    d.pop('cake')
    print(d)
    d['fruit'] = 'Mango'
    print(d.keys())
    print(d.values())
    x = 'cake' in d.keys()
    y = 'Mango' in d.values()
    print(x)
    print(y)

#Dictionaries2
def dic2():
    d = {}
    d['name'] = 0
    d['city'] = 0
    d['cake'] = 0
    for k in d.keys():
        d[k] = k.lower().count('t')
    for key, value in d.items():
        print(key, value)

#sets1
def set1():
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(21):
        if i % 2 == 0:
            s2.add(i)
        if i % 3 == 0:
            s3.add(i)
        if i % 4 == 0:
            s4.add(i)
    print(s2)
    print(s3)
    print(s4)

    if s3.issubset(s2):
        print("True")
    else:
        print("False")

    if s4.issubset(s2):
        print("True")
    else:
        print("False")

#set2
def set2():
    s = set (['p','y','t','h','o','n'])
    s.add('i')
    fs = frozenset(('m','a','r','a','t','h','o','n'))
    x = s.union(fs)
    y = s.intersection(fs)
    print(x)
    print(y)