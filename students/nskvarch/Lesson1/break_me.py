
#Break_me.py, created by Niels Skvarch
#designed to cause certain errors, commented out to expose only one error at a time


#Break for NameError:
#notbroken = ("I'm not Broken")
#Print(broken)

#Break for TypeError
#a = 10
#b = "12"
#x = a + b
#print(x)

#Break for SyntaxError:
#def adder(x)int
#return x * 2

#Break for AttrbuteError
class Atribguy(object):
	""" An Object to attach attributes to break"""
	def __init__(self):
		print("self")
		
	def one(self):
		print("yay an attibute")
		
guy1 = Atribguy()

guy1.one()
guy1.onee()

