from mailroom_lesson9 import Donor
from mailroom_lesson9 import IO
from mailroom_lesson9 import Processing

donor_dict = {'William Gates': [100.00, 100.00, 100.00], 'Mark Zuckerberg': [20.00, 20.00],
                  'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00]}
donor1 = Donor('William', 'Gates', [100.00, 100.00, 100.00])
donor2 = Donor('Mark', 'Zuckerberg', [20.00, 20.00])
donor3 = Donor('Jeff', 'Bezos', [50.00, 50.00, 50.00, 50.00, 50.00])
donor4 = Donor('Paul', 'Allen', [200.00])
donor5 = Donor('Paul', 'Allen', [200.00])
donor_list = [donor1, donor2, donor3, donor4]

# user = input("type")
# name,last = user.split()
print(donor5)
print(donor4)
assert str(donor4) == str(donor1)


