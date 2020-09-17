# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01
# Task 1: Exploring Errors (break_me.py)
# Steve Long 2020-09-10

# /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/break_me.py

def runWithNameError():
	"""
	Throws NameError because the referenced symbols are undefined.
	""" 
	print("Evaluating expression 'selfSealingStemBolt == fluxCapacitor'")
	return (selfSealingStemBolt == fluxCapacitor)

def runWithTypeError():
	"""
	Throws TypeError because the multiplication operator requires two numeric values.
	"""
	print("Evaluating expression '\"2\" * \"many\"'")
	return ("2" * "many")
	
def runWithSyntaxError():
	"""
	Throws SyntaxError because the text of the 59th Rule of Acquisition is not a valid 
	Python expression for the eval function.
	"""
	print("Evaluating expression '\"Free advice is seldom cheap.\"'")
	d = eval("Free advice is seldom cheap.")
	return d
	
def runWithAttributeError():
	"""
	Throws AttributeError because a string does not have an append method.
	"""
	print("Evaluating expression'a = \"fred\".append(9)'")
	a = "fred".append(9)
	return a

def break_me(exCode):
	"""
	break_me(<exCode>)
	
	Trap a method which throws a specific runtime error.
	
	Entry:	<exCode>	::= "ne" for NameError
							"te" for TypeError
							"se" for SyntaxError
							"ae" for AttributeError
						
	Exit:	Prints description of error, error type name, and specific error message for a 
			supported <exCode>.
	"""
	try:
		exCode = exCode.lower()
		if exCode == "ne":
			runWithNameError()
		elif exCode == "te":
			runWithTypeError()
		elif exCode == "se":
			runWithSyntaxError()
		elif exCode == "ae":
			runWithAttributeError()
		else:
			print("Arg \"{}\" is not a code for a break_me error scenario".format(exCode))
	except NameError as err:
		print("NameError: {}".format(err))
	except TypeError as err:
		print("TypeError: {}".format(err))
	except SyntaxError as err:
		print("SyntaxError: {}".format(err))
	except AttributeError as err:
		print("AttributeError: {}".format(err))
	else:
		print("No Error, no Exception")
	finally:
		print("")

print("Begin 'break_me'\n")

# Test all supported scenarios
		
break_me("ne")
break_me("te")
break_me("se")
break_me("ae")

print("End 'break_me'\n")
	