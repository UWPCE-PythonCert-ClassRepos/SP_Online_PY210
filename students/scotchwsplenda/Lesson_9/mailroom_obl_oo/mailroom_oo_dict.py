from operator import itemgetter


class Donor():

    def __init__(self, donations=[]):
        self.donations = donations

    def thanks_mail(self, name, amount):
        email = ''.join((
            "\nDear {},\n",
            "Thanks for the ${:.2f} bucks.\n",
            "We'll spend it real good baby.\n"
            )).format(name, amount)
        return email


class DonorCollection(object):

    def __init__(self, content=[]):
        self.content = []
        self.donor_db = {}
# this has to be here or it won't work in cli_main
        self.loadup()

    def add_contribution(self, name, amount):
        if self.donor_db.get(name):
            # is in donor_db already
            if isinstance(amount, list):
                self.donor_db[name].extend(amount)  # if list
            else:
                self.donor_db[name].extend([amount])  # if float
        else:
            # not in donor_db yet
            if isinstance(amount, list):
                self.donor_db[name] = amount
            else:
                self.donor_db[name] = [amount]
        return self.donor_db

    def loadup(self):
        self.add_contribution("Gordian", [30.0, 45.0])
        self.add_contribution("Maximus", [65.0, 12.0])
        self.add_contribution("Tacitus", [33.0, 22.0, 25.00])
        self.add_contribution("Commodus", [43.0, 11.0])

    def donor_names(self):
        [k for k in self.donor_db.items()]

    def data_metrics(self):
        total_giv = [(name, sum(donat), len(donat),
                     round((sum(donat)/len(donat)), 1))
                     for (name, donat) in self.donor_db.items()]
        ranked_d = sorted(total_giv, key=itemgetter(1), reverse=True)
        print('Name'+'-'*30+'Sum'+'-'*28+'Count'+'-'*30+'Avg')
        for a, b, c, d in ranked_d:
            print(f'{a:<33}{b:<33}{c:<33}{d:<33}')
        return ranked_d

    def mass_mail(self):
        for key, value in self.donor_db.items():
            with open(f'{key}.txt', 'w') as f:
                sumy = str(sum(value))
                f.write(f'Thanks {key} for donating ${sumy}.'
                        ' Your mother would be so proud.')
