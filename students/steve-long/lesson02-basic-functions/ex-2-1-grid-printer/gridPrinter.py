#!/usr/bin/env python3
# ========================================================================================
# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson02
# Grid Printer Exercise (gridPrinter.py)
# Steve Long 2020-09-20 | v0
#
# Requirements:
# -------------
#
# (Paraphrased due to pictorial nature of requirements and mix of non-requirement subject
# matter.)
#
# Part 1: Write a function that renders an NxN cell grid to stdio with "-" for the 
# horizontal cell edge, "|" for the vertical cell edge, "+" for cell nodes (intersections 
# of horizontal and vertical cell edges.)
#
# Part 2: Write a function print_grid(n) that takes one integer argument and prints a grid  
# just like before, but the size of the NxN cell grid is given by the argument, n. This is 
# an underspecified requirement that allows some degree of freedom.
#
# Part 3: Write a function print_grid2(n,m) similar to print_grid that takes an integer  
# argument n for the number of grid cells, and m for the number of characters for the  
# horizontal and vertical side of each cell. This is also an underspecified requirement  
# that allows some degree of freedom.
#
# Implementation:
# ---------------
#
#	Part 1 and 2 are implemented in function print_grid. Part 3 is implemented in 
# 	function print_grid2. The main (script-level) method calls print_grid2 and uses
# 	several helper methods to provide default and preferred values. Both print_grid and
# 	print_grid2 both call the general method makeGrid to create the grid string.
#
# Script Usage:
# -------------
#
# 	python gridPrinter.py [<cellCount> [ <cellSize>]]
#		<cellCount> ::= Number of grid cells.
#		<cellSize>  ::= Number of characters (not counting nodes) on a cell side.
#
# Issues:
# -------
#
#	If Python has something akin to Java's StringBuffer class, this would probably be
#	a good candidate for its use.
#
# History:
# --------
# 000/2020-09-20/sal/Created.
# ========================================================================================

import sys

def minCellCount():
	"""
	minCellCount()
	--------------------------------------------------------------------------------------
	Minimum number of cells N to draw for an NxN grid.
	Exit:  Returns int value > 0.
	"""
	return 1
	
def cellCountDefault():
	"""
	cellCountDefault()
	--------------------------------------------------------------------------------------
	Default number of cells N to draw for an NxN grid.
	Exit:  Returns int value > 0.
	"""
	return 2

def minCellSize():
	"""
	minCellSize()
	--------------------------------------------------------------------------------------
	Smallest number of characters M for a cell edge on an NxN grid (not counting node 
	character).
	Exit:  Returns int value > 0.
	"""
	return 1
	
def cellSizeDefault():
	"""
	cellSizeDefault()
	--------------------------------------------------------------------------------------
	Default number of characters M for a cell edge on an NxN grid (not counting node 
	character).
	Exit:  Returns int value > 0.
	"""
	return 4
	
def edgeCharHDefault():
	"""
	edgeCharHDefault()
	--------------------------------------------------------------------------------------
	Default character for a cell horizontal edge on an NxN grid (not counting node 
	character).
	Exit:  Returns single char.
	"""
	return "-"
	
def edgeCharVDefault():
	"""
	edgeCharVDefault()
	--------------------------------------------------------------------------------------
	Default character for a cell vertical edge on an NxN grid (not counting node 
	character).
	Exit:  Returns single char.
	"""
	return "|"
	
def nodeCharDefault():
	"""
	nodeCharDefault()
	--------------------------------------------------------------------------------------
	Default character where cell horizontal and vertical edges intersect on an NxN grid.
	Exit:  Returns single char.
	"""
	return "+"
	
def isValidNodeChar(nodeChar):
	"""
	isValidNodeChar(<nodeChar>)
	--------------------------------------------------------------------------------------
	Validation rule for node character on NxN grid.
	Entry: <nodeChar> ::= A single character.
	Exit:  Returns True if valid.
	"""
	valid = (len(nodeChar) == 1)
	return valid
	
def isValidEdgeCharH(edgeCharH):
	"""
	isValidEdgeCharH(<edgeCharH>)
	--------------------------------------------------------------------------------------
	Validation rule for cell horizontal edge character on NxN grid.
	Entry: <edgeCharH> ::= A single character.
	Exit:  Returns True if valid.
	"""
	valid = (len(edgeCharH) == 1)
	return valid
	
def isValidEdgeCharV(edgeCharV):
	"""
	isValidEdgeCharV(<edgeCharV>)
	--------------------------------------------------------------------------------------
	Validation rule for cell vertical edge character on NxN grid.
	Entry: <edgeCharV> ::= A single character.
	Exit:  Returns True if valid.
	"""
	valid = (len(edgeCharV) == 1)
	return valid
	
def gridLineEdgeH(cellCount, cellSize, nodeChar, edgeCharH):
	"""
	gridLineEdgeH(<cellCount>, <cellSize>, <nodeChar>, <edgeCharH>)
	--------------------------------------------------------------------------------------
	Draw a horizontal line for the grid.
	Entry:	<cellCount> ::= Grid cell count (N).
			<cellSize>  ::= Grid cell edge size.
			<nodeChar>  ::= Character for grid node.
			<edgeCharH> ::= Character for cell horizontal edge.
	Exit:   Returns string rendering for grid horizontal line.
	"""
	s = nodeChar
	for i in range(0, cellCount):
		s = "{}{}{}".format(s, (edgeCharH * cellSize), nodeChar)
	return s
	
def gridLineEdgeV(cellCount, cellSize, nodeChar, edgeCharV):
	"""
	gridLineEdgeV(<cellCount>, <cellSize>, <nodeChar>, <edgeCharV>)
	--------------------------------------------------------------------------------------
	Draw a vertical line for the grid.
	Entry:	<cellCount> ::= Grid cell count (N).
			<cellSize>  ::= Grid cell edge size.
			<nodeChar>  ::= Character for grid node.
			<edgeCharV> ::= Character for cell vertical edge.
	Exit:   Returns string for grid vertical line.
	"""
	s = edgeCharV
	for i in range(0, cellCount):
		s = "{}{}{}".format(s, (" " * cellSize), edgeCharV)
	return s
	
def makeGrid(cellCount, cellSize, nodeChar, edgeCharH, edgeCharV):
	"""
	makeGrid(<cellCount>, <cellSize>, <nodeChar>, <edgeCharH>, <edgeCharV>)
	--------------------------------------------------------------------------------------
	Build the string need to rend an NxN grid.
	Entry:	<cellCount> ::= Grid cell count (N). No less than minCellCount().
			<cellSize>  ::= Grid cell edge size. No less than minCellCount().
			<nodeChar>  ::= Single character for grid node. 
			<edgeCharH> ::= Single character for cell horizontal edge.
			<edgeCharV> ::= Single character for cell vertical edge.
	Exit:   Returns string for grid. Invalid argument values are replaced by minimum or
			default values.
	"""
	cellCount = max(minCellCount(), cellCount)
	cellSize = max(minCellSize(), cellSize)
	nodeChar = nodeChar if isValidNodeChar(nodeChar) else nodeCharDefault()
	edgeCharH = edgeCharH if isValidEdgeCharH(edgeCharH) else edgeCharHDefault()
	edgeCharV = edgeCharV if isValidEdgeCharV(edgeCharV) else edgeCharVDefault()
	s = gridLineEdgeH(cellCount, cellSize, nodeChar, edgeCharH) + "\n"
	for i in range(0,cellCount):
		for j in range(0,cellSize):
			s = s + gridLineEdgeV(cellCount, cellSize, nodeChar, edgeCharV) + "\n"
		s = s + gridLineEdgeH(cellCount, cellSize, nodeChar, edgeCharH) + "\n"
	return s

def print_grid(cellCount):
	"""
	print_grid(<cellCount>)
	--------------------------------------------------------------------------------------
	Draw an N-cell grid.
	Entry:	<cellCount> ::= Grid cell count (N).
	Exit:   Renders NxN grid with default cell edge size to standard output.
	"""
	s = makeGrid(cellCount, cellSizeDefault, nodeCharDefault(), edgeCharHDefault(), edgeCharVDefault())
	print(s)
		
def print_grid2(cellCount, cellSize):
	"""
	print_grid2(<cellCount>, <cellSize>)
	--------------------------------------------------------------------------------------
	Draw an N-cell grid of M-sized cells.
	Entry:	<cellCount> ::= Grid cell count (N).
			<cellSize>  ::= Grid cell edge size (M).
	Exit:   Renders Renders NxN grid with specified cell edge size to standard output.
	"""
	s = makeGrid(cellCount, cellSize, nodeCharDefault(), edgeCharHDefault(), edgeCharVDefault())
	print(s)

# Command-line interface for demonstrating function print_grid2.
#
# Usage: python gridPrinter.py [<cellCount> [ <cellSize>]]
	
if __name__ == "__main__":
	msg = ""
	argvCount = len(sys.argv)
	if (argvCount > 3):
		print("Ignoring extra arguments")
	args = [cellCountDefault(), cellSizeDefault()]
	ok = True
	#
	# Check for invalid input; substitute with default values if not specified.
	#
	for i in range(1,min(len(sys.argv),3)):
		if (not sys.argv[i].isnumeric()):
			msg = msg + "\ngridPrinter (ERROR): Arg {} ({}) not an integer".format(i,sys.argv[i])
			ok = False
		else:
			args[i-1] = abs(int(sys.argv[i]))
	if ok:
		#
		# Draw grid OR...
		#
		cellCount = args[0]
		cellSize = args[1]
		print_grid2(cellCount,cellSize)
	else:
		#
		# ...print error message.
		#
		print(msg[1:])
	
	
	
	
	
	
	