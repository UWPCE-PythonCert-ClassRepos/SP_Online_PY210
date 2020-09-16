# Title: Str Lab
# Dev: Roslyn Melookaran
# Date: 9/15/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/15/20, created script)
# --------------------------------------------------------------
def formatter(string,touple):
    count=len(touple)
    string="the "+count+" numbers are: "
    for i in range(count):
        str
t=(2, 123.4567, 10000, 12345.67)
# -------TASK 1--------#
print('file{:0>3}: {:.2f}, {:.2e}, {:.3g}'.format(t[0], t[1], t[2], t[3]))
print('file{:0>3}: {:.2f}, {:.2e}, {:.3g}'.format(*t)) #Trimmed down version
# -------TASK 2--------#
print(f"file{t[0]:0>3}: {t[1]:.2f}, {t[2]:.2e}, {t[3]:.3g}")
# -------TASK 3--------#
x=(1, 2, 3,5, 6)
string=""

