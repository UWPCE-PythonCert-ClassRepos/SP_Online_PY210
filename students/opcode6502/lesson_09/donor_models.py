# donor_models.py
# opcode6502: SP_Online_PY210


class Donor:

    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = donations

    def add_donation(self, donation=[]):
        self.donations.extend(donation)


class DonorCollection:
    pass
