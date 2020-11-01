#!/usr/bin/env python3

import io
import math

from Donor_Models import Donor, Donor_Collect  

'''Initial setup'''

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
MS.append([0.01, 20.00])
CV.append([800, 15, 10.00])
JDR.append([7000, 150.00, 25])
SG.append([60000])
AC.append([0.04, 999.99])


if __name__ == "__main__":
    print(don_col)