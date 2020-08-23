def firstLast(seq):
	""" switches the first and last values of a sequence"""
	seq1 = seq[-1:] + seq[1:-1] + seq[:1]
	return seq1

def everyOther(seq):
	seq1 = seq[0:-1:2]
	return seq1