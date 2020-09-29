#/usr/bin/env python3

def name_error():
	undefined_function()


def type_error():
	return "a" % "b"


#def syntax_error():
	#return [1  3 42]

def attribute_error():
	"a".append(2)	
	
		
