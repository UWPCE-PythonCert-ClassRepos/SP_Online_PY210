# #!/usr/bin/env python3

import sys

donor_db = {
    "Jeff Staple": [20, 20],
    "Takashi Murakami": [10.50],
    "Virgil Abloh": [300, 40.33, 5.35],
    "Jan Chipchase": [1001.23, 400.87, 102]
}

# user_key = str(input("enter a name: "))
# user_key = user_key.title()
# if user_key in donor_db.keys():
#     donats = donor_db[user_key]
#     summer = sum(donats)
#     print(summer)
#     namer = user_key.split(" ")
#     firster = namer[0]
#     print(firster)

for item in donor_db:
    donats = donor_db[item]
    donats.append(10.00)
    print(donats)

# else:
#     print("no dice")
