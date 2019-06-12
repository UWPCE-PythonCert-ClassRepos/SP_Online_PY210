
def first_and_last(seq):
      return seq[-1:] + seq[1:-1] + seq[:1]
myseq = first_and_last("Reverse the order of words")
print(myseq)

def rem_item(seq):
       return seq[::2]
myseq1 = rem_item("Reverse the order of words")
print(myseq1)

def rem_four(seq):
        return seq[4:-4:2]
myseq2 = rem_four("Reverse the order of words")
print(myseq2)

def swap_words(seq):
      return(' '.join(seq.split()[::-1]))
myseq3 =swap_words("Reverse the order of words")
print(myseq3)

def mix_items(seq):
#    ofs =(len(seq)//2
    return seq.strip()[0:-3:3]
myseq4 = mix_items("Reverse the order of words")
print(myseq4)

