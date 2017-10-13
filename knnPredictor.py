import csv
import operator
import random
import itertools
import math, statistics

def loadDataSet(filename, split, trainingSet = [], testSet=[]):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        next(lines, None)
        dataset = list(lines)

        for a in range(len(dataset)-1):
            if (dataset[a][-1] == '2' or dataset[a][-1] == '3' or dataset[a][-1] == '4'):
                dataset[a][-1] = '1'

        for x in range(len(dataset)-1):
            for y in range(13):
                if(dataset[x][y] == ' '):
                    for a in range(len(dataset)-1):
                        median_list = []
                        median_list.append(dataset[a][y])
                    dataset[x][y] = float(statistics.median(median_list))
                try:
                    dataset[x][y] = float(dataset[x][y])
                except ValueError:
                    pass

            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        try:
            distance += pow((instance1[x] - instance2[x]), 2)
        except TypeError:
            pass
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

