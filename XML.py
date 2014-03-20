#!/usr/bin/env python

#--------------
# XML.py
#--------------


from xml.etree.ElementTree import Element, fromstring, tostring, SubElement
import sys

x = 1
tot = 0

def numchild (a) :
	n = 0
	for v in a :
		n += 1
	return n

def match (a, b) :
	if a.tag != b.tag :
		return "false"
	if numchild (b) == 0 :
		return "true"
	for v in a :
		if numchild (b) > 0 :
			if match (v, b[0]) == "true" :
				return "true"
	return "false"

def traverse (a, opt) :
	global x
	global tot
	
	if match (a, q) == "true" :
		if opt == 0 :
			tot += 1
		else :
			print(str(x))

	for v in a :
		x += 1
		traverse(v, opt)

def read(r) :
	s = "<xml>" + "".join(r) + "</xml>"
	assert(type(s) is str)

	a = fromstring(s)
	assert(type(a) is Element)

	return a

a = read(sys.stdin)
q = a[1]
#for n in a.findall("."):
def main() :
	global x
	global tot
	
	traverse(a[0], 0)
	print(tot)
	x = 1
	traverse(a[0], 1)