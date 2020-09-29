def display_items(seq):
	l = len(seq)
	print(("there are {} items and they are:" + ",".join(["{}"] * l)).format(l, *seq))
