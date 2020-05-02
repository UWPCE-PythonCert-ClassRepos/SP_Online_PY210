#!/usr/bin/env python3

"""
Donor Class
Class responsible for donor data encapsulation

This class will hold all the information about a single donor, 
and have attributes, properties, and methods to provide access 
to the donor-specific information that is needed. Any code that 
only accesses information about a single donor should be part 
of this class.

DonorCollection Class
Class responsible for donor collection data encapsulation

This class will hold all of the donor objects, as well as methods 
to add a new donor, search for a given donor, etc. If you want a 
way to save and re-load your data, this class would hold that 
method, too.

Your class for the collection of donors will also hold the code 
that generates reports about multiple donors.

In short: if the functionality involves more than one donor – 
it belongs in this class.

Note that the DonorCollection class should be holding, and 
working with, Donor objects – it should NOT work directly with 
a list of donations, etc.
"""

class Donor(object):
    # Class responsible for donor data encapsulation
    pass

class DonorCollection(object):
    # Class responsible for donor collection data encapsulation
    pass