#--------------------------------------------------------------#
# Title: Lesson 3,
# Description: Fun slicing sequences
# ChangeLog (Who,When,What):
# JEmbury, 9/19/2020, created new script
#--------------------------------------------------------------#

def exchange_first_last(seq):
    new_seq = seq[1:-1]
    new_seq.append(seq[0])
    new_seq.insert(0,seq[-1])
    return new_seq

#--------------------------------------------------------------#
if __name__ == '__main__':
    (exchange_first_last('hello there')