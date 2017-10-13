from knnPredictor import loadDataSet, getNeighbors, getResponse

def userData():
    age = float(input("Enter age:"))
    sex = float(input("Enter sex:"))
    cp = float(input("Enter cp:"))
    trestbps = float(input("Enter trestbps:"))
    chol = float(input("Enter chol:"))
    fbs = float(input("Enter fbs:"))
    restecg = float(input("Enter restecg:"))
    thalach = float(input("Enter thalach:"))
    exang = float(input("Enter exang:"))
    oldpeak = float(input("Enter oldpeak:"))
    slope = float(input("Enter slope:"))
    ca = float(input("Enter ca:"))
    thal = float(input("Enter thal:"))

    testData = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope,ca, thal]
    return testData

def main():
    trainingData = []
    testSet = []

    testData = userData()
    print("This is", testData)

    loadDataSet('pc.csv', 1, trainingData, testSet)

    print('Train Data:' + repr(len(trainingData)))
    print('Test Data:' + repr(len(testSet)))

    k = 11
    neighbor = getNeighbors(trainingData, testData, k)
    result = getResponse(neighbor)
    prediction = result
    print('predicted result is ', prediction)


main()




