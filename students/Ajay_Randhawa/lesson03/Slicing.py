def firstLast(seq):
	""" switches the first and last values of a sequence"""
	seq1 = seq[-1:] + seq[1:-1] + seq[:1]
	return seq1

def everyOther(seq):
	""" using the step function to return
	every other item in sequence"""
	seq1 = seq[0:-1:2]
	return seq1

def function3(seq):
	"""removes first 4 and last 4 items, and
	then evey other item"""
	seq1 = seq[4:-4:2]
	return seq1