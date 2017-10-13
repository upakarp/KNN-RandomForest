from knnPredictor import *
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def main():
    # prepare data
    temp = []
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataSet('pc.csv', split, trainingSet, testSet)
    print('Train set:' + repr(len(trainingSet)))
    print('Test set:' + repr(len(testSet)))
    # generate predictions
    predictions = []
    actual = []
    k = 11
    for x in range(len(testSet)):
        temp.append(float(testSet[x][-1]))
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        actual.append(testSet[x][-1])
        print(('>predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1])))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

    print("Confusion matrix is : ")
    print(confusion_matrix(actual, predictions))

    # plt.plot(predictions, 'ro', ms=2)
    # plt.plot(temp, 'ko', ms=1.5)
    # plt.show()

main()