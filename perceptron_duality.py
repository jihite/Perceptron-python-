import os
import sys
 
# An example in that book, the training set and parameters' sizes are fixed
training_set = []
 
w = []
a = []
b = 0
lens = 0
n = 0
Gram = []
 
def calInnerProduct(i, j):
	global lens
	res = 0
	for p in range(lens):
		res += training_set[i][0][p] * training_set[j][0][p]
	return res

def AddVector(vec1, vec2):
	for i in range(len(vec1)):
		vec1[i] = vec1[i] + vec2[i]
	return vec1
	
def NumProduct(num, vec):
	for i in range(len(vec)):
		vec[i] *= num
	return vec 

def createGram():
	global lens
	for i in range(len(training_set)):
		tmp = []
		for j in range(0, len(training_set)):
			tmp.append(calInnerProduct(i, j))
		Gram.append(tmp)

# update parameters using stochastic gradient descent
def update(k):
	global a, b, n
	a[k] += n
	b = b + n * training_set[k][1] 
	print a, b # you can uncomment this line to check the process of stochastic gradient descent
 
# calculate the functional distance between 'item' an the dicision surface
def cal(k):
	global a, b
	res = 0
	for i in range(len(training_set)):
		res += a[i] * int(training_set[i][1]) * Gram[i][k]
	res += b
	res *= training_set[k][1]
	return res
 
# check if the hyperplane can classify the examples correctly
def check():
	global w, a
	flag = False
	for i in range(len(training_set)):
		if cal(i) <= 0:
			flag = True
			update(i)

	if not flag: #False
		for i in range(len(training_set)):
			w = AddVector(w, NumProduct(a[i] * int(training_set[i][1]), training_set[i][0]))
		print "RESULT: w: ", w, " b: ", b
		tmp = ''
		for keys in w:
			tmp += str(keys) + ' '
		tmp = tmp.strip()
		modelFile.write(tmp + '\n')
		modelFile.write(str(b) + '\n')
		modelFile.write(str(lens) + '\n')
		modelFile.write(str(n) + '\n')
		modelFile.close()
		os._exit(0)
	flag = False
 
if __name__=="__main__":
	if len(sys.argv) != 4:
		print "Usage: python perceptron_duality.py n trainFile modelFile"
		exit(0)
	n = float(sys.argv[1])
	trainFile = file(sys.argv[2])
	modelFile= file(sys.argv[3], 'w')
	lens = 0
	for line in trainFile:
		chunk = line.strip().split(' ')
		lens = len(chunk) - 1
		tmp_all = []
		tmp = []
		for i in range(1, lens+1):
			tmp.append(int(chunk[i]))
		tmp_all.append(tmp)
		tmp_all.append(int(chunk[0]))
		training_set.append(tmp_all)
	trainFile.close()
	  
	createGram()
	for i in range(len(training_set)):
		a.append(0)
	for i in range(lens):
		w.append(0)
	
	for i in range(1000):
		check()
	print "The training_set is not linear separable. "
