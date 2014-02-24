import os
import sys
 
# An example in that book, the training set and parameters' sizes are fixed
training_set = []
 
w = []
b = 0
lens = 0
n = 0
 
def cal(item):
	global w, b, lens
	res = 0
	for i in range(lens):
		res += item[i] * w[i]
	res += b
	return res
 
if __name__=="__main__":
	if len(sys.argv) != 4:
		print "Usage: python predict.py testFile modelFile outFile"
		exit(0)
	testFile = file(sys.argv[1])
	modelFile= file(sys.argv[2])
	outFile = file(sys.argv[3], 'w')
	line1 = modelFile.readline().strip()
	line2 = modelFile.readline().strip()
	line3 = modelFile.readline().strip()
	line4 = modelFile.readline().strip()
	chunk = line1.strip().split(' ')
	for key in chunk:
		w.append(float(key))
	b = float(line2)
	lens = int(line3)
	n = float(line4)
		
	for line in testFile:
		chunk = line.strip().split(' ')
		tmp = []
		for i in range(1, lens+1):
			tmp.append(int(chunk[i]))
		re = cal(tmp)
		if re > 0:
			outFile.write('+1\n')
		else:
			outFile.write('-1\n')
	outFile.close()
	testFile.close()
