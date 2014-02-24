from __future__ import division
import linecache
import sys
import os
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "Usage: python evaluate.py outFile goldFile"
		exit(0)
	outFile = file(sys.argv[1])
	goldFile = sys.argv[2]
	tt = 0
	tf = 0
	ft = 0
	ff = 0
	count = 1
	for line in outFile:
		my = int(line.strip())
		gold = int(linecache.getline(goldFile, count).strip())
		print "my", my
		print "gold", gold
		count += 1
		if my == 1:
			if gold == 1:
				tt += 1
			else:
				ft += 1
		else:
			if gold == 1:
				tf += 1
			else:
				ff += 1
	p = tt / (tt + ft) 
	r = tt / (tt + tf)
	f = 2 * p * r / (p + r)
	print "tt:", tt
	print "tf:", ft
	print "ff:", ff
	print "ft:", ft
	print "p:", p
	print "r:", r
	print "f:", f
	
