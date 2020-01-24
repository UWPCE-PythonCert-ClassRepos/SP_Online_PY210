# #!/usr/bin/env python3
#
# feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
#
# comprehension = [delicacy.capitalize() for delicacy in feast]
#
# print(comprehension[0])

# donor_db = {
#     "Jeff Staple": [20, 20],
#     "Takashi Murakami": [10.50],
#     "Virgil Abloh": [300, 40.33, 5.35],
#     "Jan Chipchase": [1001.23, 400.87, 102]
# }
#
# comprehension = [name.strip().lower() for name in donor_db]
#
# print(comprehension[2])
#
# feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
#
# comp = [delicacy for delicacy in feast if len(delicacy) > 6]
#
# print(len(feast))
#
# print(comp)
#
# eggs = ['poached egg', 'fried egg']
#
# meats = ['lite spam', 'ham spam', 'fried spam']
#
# comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
#
# print(comprehension[0])
#
# comprehension = {c for c in 'aabbbcccc'}
#
# print(comprehension)

dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third': 'ruthless efficiency', 'forth': 'fanatical devotion',
                   'fifth': None}
dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

print(len(dict_comprehension))
