#!/usr/bin/env python3

import io
import math

from Donor_Models import Donor, Donor_Collect  

'''Initial setup'''
'''
donors = {"Morgan Stanely": [0.01, 20.00],
            "Cornelius Vanderbilt": [800, 15, 10.00],
            "John D. Rockefeller": [7000, 150.00, 25],
            "Stephen Girard": [60000],
            "Andrew Carnegie": [0.04, 999.99],}
'''

don_col = Donor_Collect()
MS = Donor("Morgan Stanley")    
CV = Donor("Cornelius Vanderbilt")
JDR = Donor("John D. Rockefeller")
SG = Donor("Stephen Girard")
AC = Donor("Andrew Carnegie")
don_col.append(MS)
don_col.append(CV)
don_col.append(JDR)
don_col.append(SG)
don_col.append(AC)


if __name__ == "__main__":
    print(don_col)