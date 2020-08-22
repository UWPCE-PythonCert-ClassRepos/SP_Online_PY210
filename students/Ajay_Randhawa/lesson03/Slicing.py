def firstLast(seq):
	""" switches the first and last values of a sequence"""
	seq1 = seq[:]
	seq[0] = seq1[-1]
	seq[-1] = seq1[0]
	return seq