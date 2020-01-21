donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

name_donat = ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])

namer = name_donat[0]
namer = namer.split()
firster = namer[0]
monies = name_donat[1]
toters = sum(monies)

letter = ('\n'.join(['','Dearest {first_name},', '', 'Thank you for your generous support!',
                     'We appreciate your donation(s), which total ${donats:.2f} to date!', '', 'Sincerest regards', '',
                     'The Foundation'])).format(first_name=firster,donats=toters)

print("Here is your Thank You:")
print(letter)

