from sklearn.metrics import confusion_matrix

from knnPredictor import *
import itertools, random, pandas, csv

lst = [0,1,2,3,4,5,6,7,8,9,10,11,12]
cmb = list(itertools.combinations(lst,7))

length = len(cmb)
print (length)
#testdata = pandas.read_csv("pc.csv", usecols=cmb[2])
trainingSet = []
testSet = []
'''
with open("pc.csv", 'rt') as csvfile:
        lines = csv.reader(csvfile)
        next(lines, None)
        dataset = list(lines)
        for x in range(len(dataset)-1):
        	for k in range(13):
        		for y in range(13):
        			try:
        				dataset[x][y] = float(dataset[x][y])
        			except ValueError:
        				pass
        		if random.random() < 0.67:
        			trainingSet.append(dataset[x])
        		else:
        			testSet.append(dataset[x])
'''
with open("pc.csv",'rt') as csvfile:
	lines = csv.reader(csvfile)
	next(lines, None)
	dataset = list(lines)
	i=0
	utmost_accuracy=0.0
	utmost_cmb = []

	best_prediction = []
	best_actual = []

	for i in range(0,5):
		for x in range(len(dataset)-1):
			tuple_hp = (dataset[x][-1], None)
			test = cmb[i]+tuple_hp
			for k in range(0,8):
				try:
					dataset[x][int(test[k])] = float(dataset[x][int(test[k])])
				except ValueError:
					pass
			if random.random() < 0.67:
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])
		predictions = []
		actual = []
		k = 11
		for x in range(len(testSet)):
			neighbors = getNeighbors(trainingSet, testSet[x], k)
			result = getResponse(neighbors)
			predictions.append(result)
			actual.append(testSet[x][-1])
			print(('>predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1])))
		accuracy = getAccuracy(testSet, predictions)
		print('Accuracy: ' + repr(accuracy) + '%')
		if accuracy>utmost_accuracy:
			utmost_accuracy = accuracy
			utmost_cmb = cmb[i]
			best_prediction.append(predictions)
			best_actual.append(actual)

	print ("utmost accuracy is ",utmost_accuracy)
	print ("best combination is ", utmost_cmb)
	testdata = pandas.read_csv("pc.csv", usecols=utmost_cmb)
	utmost_list = list(testdata)
	print (utmost_list)

	print("Best prediction is", best_prediction)
	print("Best acutal is", best_actual)
	print("Last best prediction is", best_prediction[-1])
	print("Last best actual is", best_actual[-1])

	print("Confusion matrix is")
	print(confusion_matrix(best_prediction[-1], best_actual[-1]))

