donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]


def report(db=donor_db):
    print(donor_db)
    print()
    key = ["name", "total given", "num gifts", "average gift"]
    separator = "|"

    print(f"{key[0]:<18}",
          f"{separator:^3}",
          f"{key[1]:<18}",
          f"{separator:^3}",
          f"{key[2]:>10}",
          f"{separator:^3}",
          f"{key[3]:>15}")
    print("-"*76)

    for i in range(0, (len(donor_db))):
        entry = (donor_db[i])
        name = entry[0]
        # print(name)
        dons = entry[1]
        totes = sum(dons)
        # print(totes)
        nums = len(dons)
        # print(nums)
        aves = totes/nums
        # print(aves)
        print(f"{name:<18}",
          f"{separator:^3}",
          f"{totes:>18.2f}",
          f"{separator:^3}",
          f"{nums:^10}",
          f"{separator:^3}",
          f"{aves:>15.2f}")

report()

# print(type(donor_db[0]))
