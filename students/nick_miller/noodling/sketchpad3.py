donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]


def nameslist(db=donor_db):
    names = []
    for i in range(0, (len(donor_db))):
        entry = (donor_db[i])
        name = entry[0]
        names.append(name.lower())


print(type(nameslist()))