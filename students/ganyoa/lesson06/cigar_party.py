#!/usr/bin/env python

def cigar_party(cigars, is_weekend):
#    pass


  if not is_weekend and 40 <= cigars <= 60:
    return True
  if is_weekend and cigars >= 40:
    return True
  return False
