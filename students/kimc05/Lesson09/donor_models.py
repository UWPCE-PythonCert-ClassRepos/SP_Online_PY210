"""
Christine Kim
Lesson 9
Donor Class
"""

class Giver():

    #initialize Giver
    def __init__(self, name, donation=None):
        self.name = name
        try:
            self.donations = [d for d in donation]
        except TypeError:
            self.donations = [donation]

    #compare
    def __lt__(self, other):
        if self.total_v() < other.total_v():
            return  True
        elif self.total_v() == other.total_v():
            return self.avg() < other.avg()
        else:
            return False

    def __eq__(self, other):
        return self.total_v() == other.total_v() and self.avg() == other.avg()

    #return number of donations given
    def num_give(self):
        return len(self.donations)

    #return total value of donations given
    def total_v(self):
        total_given = 0
        for instance in self.donations:
            total_given += instance
        return total_given

    #return average value of donations given
    def avg(self): 
        return self.total_v() / self.num_give()

    #summarize donor info
    def summary(self):
        return "{:<30}${:>15.2f}{:>10} ${:>15.2f}\n".format(self.name, self.total_v(), self.num_give(), self.avg())

    #write email
    def gratitude(self, amt):
        return (f"\nDear Ser {self.name},\n"
                    f"Thank you for your generous donation of ${amt:,d}\n"
                    "We will make certain your goodwill is directed to aid those affected by the Fifth Blight.\n"
                    "With regards,\n"
                    "The Blight Orphans Charity,\n") 

# -----------------------------------------------------------------------------

class GiverCollection(Giver):
    #initialize dict of current givers
    def __init__(self, dict_givers):
        self.givertree = dict_givers

    def dict_givers(self):
        return self.givertree

    def num_givers(self):
        return len(self.givertree)

    #get all donor names
    def names(self):
        return ("\n{}"*self.num_givers()).format(*self.givertree.keys())

    #add new donor
    def add_giver(self, giver, received):
        try:
            self.givertree.setdefault(giver.name, self.givertree[giver.name].donations.append(received))
        except KeyError:
            self.givertree[giver.name] = Giver(giver.name, giver.donations)

    #sort by total, average donation
    def sort_mine(self):
        return sorted(self.givertree.values(), reverse=True)

    #return string of summarized donor information
    def report_givers(self):
        for person in self.sort_mine():
            print(person.summary())