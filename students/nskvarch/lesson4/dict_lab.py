#!/user/bin/env python3
#dictionary lab created by Niels Skvarch


d = {"name" : "chris", "city" : "seattle", "cake" : "chocolate"}
d2 = d.copy()
s = set(range(0, 21, 2))
s1 = set(range(0, 21, 3))
s2 = set(range(0, 21, 4))
sp = set(["P", "y", "t", "h", "o", "n"])
sm = frozenset(["M", "a", "r", "a", "t", "h", "o", "n"])


def dictlab(d):
    """contains the body of the dictionary lab"""
    print(d)
    print("\n\n")
    d.pop("cake")
    print(d)
    print("\n\n")
    d["fruit"] = "mango"
    print(d)
    print("\n\n")
    print(d.keys())
    print("\n\n")
    print(d.values())
    print("\n\n")
    print("is cake in the dictionary?: {}".format("cake" in d.keys()))
    print("\n\n")
    print("is mango in the dictionary?: {}".format("mango" in d.values()))
    print("\n\n")


def dictlab2(d):
    """contains the body of the dictionary lab"""
    print(d)
    for key in d:
        d[key] = d[key].lower().count('t')
    print("\n\n", d, "\n\n")


def setslab(s, s1, s2, sp, sm):
    """contains the body of the sets lab"""
    print(s, "\n", s1, "\n", s2)
    print("is set 1 a subset of set 0? : {}".format(s1.issubset(s)), "\n")
    print("is set 2 a subset of set 0? : {}".format(s2.issubset(s)), "\n\n")
    print(sp, "\n")
    print(sm, "\n")
    sp.add("i")
    print(sp, "\n")
    print("union of Pythoni and Marathon : {}".format(sp.union(sm)), "\n")
    print("intersection of Pythoni and Marathon : {}".format(sp.intersection(sm)), "\n")


def main():
    dictlab(d)
    dictlab2(d2)
    setslab(s, s1, s2, sp, sm)



#main program name-space
if __name__ == "__main__":
    main()


