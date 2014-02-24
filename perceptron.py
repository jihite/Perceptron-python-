import os
import sys
 
# An example in that book, the training set and parameters' sizes are fixed
training_set = []
 
w = []
b = 0
lens = 0
n = 0
 
# update parameters using stochastic gradient descent
def update(item):
	global w, b, lens, n
	for i in range(lens):
		w[i] = w[i] + n * item[1] * item[0][i]
	b = b + n * item[1]
	print w, b # you can uncomment this line to check the process of stochastic gradient descent
 
# calculate the functional distance between 'item' an the dicision surface
def cal(item):
    global w, b
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
    res += b
    res *= item[1]
    return res
 
# check if the hyperplane can classify the examples correctly
def check():
	flag = False
	for item in training_set:
		if cal(item) <= 0:
			flag = True
			update(item)
	if not flag: #False
		print "RESULT: w: " + str(w) + " b: "+ str(b)
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
		print "Usage: python perceptron.py n trainFile modelFile"
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
	for i in range(lens):
		w.append(0)
	
	for i in range(1000):
		check()
	print "The training_set is not linear separable. "
