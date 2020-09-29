#n dimensional array numpy

import numpy as numpy

nparr = np.array(arr)

nparr[2] #second row

nparr[:, 2] #second column

nparr[1:3, 0:2]


class SimpleIndex:
    def __getitem__(self, index):
        print(type(index))
        print(index)

si = SimpleIndex()

si[2]

si["fred"]

si[1:5:2]

#gives us slice component

slice?

si[1:4, 4:6]

#gives us multiple slice objects


import operator
operator.index?

operator.index(5)

operator.index(5.5)

operator.index(np.int16(4))


# video 2 soorting

#two ways to sort

#1) sort the actual list

rand_list = list(range(10))
random.shuffle(rand_list)

rand_list.sort()


sorted(rand_list) #returns new array

#using key with function to return 2nd value to sort by last name


# Video 3 Making Custom Classes Sortable
class Donor:

    def __init__(self, name, donations):
        self.name = name
        self.donations = donations

        # not good
    def __lt__(self, other):
        if self.name < other.name:
            return True
        elif self.name == other.name:
            return True
        else:
            return False

    #pythons built in function for tuples
    def __lt__(self, other):
        return (self.name, self.donations) < (other.name, other.donations)

    @staticmethod
    def sort_key(self):
        return (self.last_name, self.first_name, self.donations)

    @staticmethod
    def sort_by_donations:
        return self.donations

    def __repr__(self):
        return "Donor({} {}, {})".format(self.first_name, self.last_name, repr(self.donations))


    sorted(donor_list, key=Donor2.sort_key)

    % timeit sorted(donor_list)
    #^used in ipython

    # timeit sorted(donor_list, key=Donor2.sort_key)
    # sort key functions are faster by about 3 times

# Video 4: Managing access to object attributes
class SimpleFighterGuy(object):
    def __init__(self):
        self.health = 100

simple_fighter_guy = SimpleFighterGuy()

simple_fighter_guy.health-= 10

another_fighter_guy = SimpleFighterGuy()

simple_army_health = simple_fighter_guy.health + another_fighter_guy.heatlh

class PropertyFighterGuy(object):

    def __init__(self):
        self.health = 100

    def get_health(self):
        return self.health

    def set_health(self, health):
        if health > 100:
            self.health = 100
        elif health < 0:
            self.health = 0
        else:
            self.health = health

    health = property(get_health, set_health)


property_fighter_guy = PropertyFighterGuy()

property_fighter_guy.health
property_fighter_guy.health += 10 #will still be 100