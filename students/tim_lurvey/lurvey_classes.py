#!/usr/bin/env python

class bunch(object):
    def __init__(self,**kwargs):
        setattr(self, '__dict__', kwargs)