#!/usr/bin/env python3

####################################################
# Lesson 08
# Steve Morehouse
####################################################

class Circle (object):

    def __init__ (self, radius):
        if radius <=0:
            raise ValueError ('radius needs to be positive')
        else:
            self.radius = float (radius)

