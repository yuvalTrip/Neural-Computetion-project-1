import random
import sys

import numpy as np
from sklearn.metrics import accuracy_score


def randomGenerator():
    """
    function create data of size 1000
    :return: list of data and list of answers
    """
    rand = []  # Create data of size 1000
    for i in range(1000000):  # with random values in range [-100,100] for x1,x2 in <x1,x2>
        rand.append((random.uniform(-100, 100), random.uniform(-100, 100)))
    answers = []
    for i in range(1000000):  # for all pairs in rand list we will check if the x2 value is >= 1
        value = rand[i][1] ** 2 + rand[i][0] ** 2
        if 4 <= value <= 9:
            # if rand[i][1] >= 1:
            answers.append(1)  # if it does, the answer will be 1
        else:
            answers.append(-1)  # if it <= -1 , the answer will be -1
    ans = np.array(answers)
    return rand, answers


def adaline(trainSet, ansTrainSet):
    """
    :param trainSet: rand list from randomGenerator function
    :param ansTrainSet: answers list from randomGenerator function
    :return: new weights w1_new, w2_new and b_new
    """
    # To write Adaline algorithm we used:
    # https://www.youtube.com/watch?v=0xnN_yf6FbU

    trainSet = np.array(trainSet)
    trainSet /= 100
    EPS = 0.5  # set an epsilon
    learningRate = 0.2  # set learning rate (should be a random number between [0,1] )
    w1_new = w2_new = 0.2  # set initial weights (should be a random numbers between [0,1] )
    b_new = 0.2
    total_MSE = sys.maxsize  # initial MSE value as the MAX number
    MSE = sys.maxsize
    while (total_MSE / len(trainSet)) - EPS > 0:  # In class, we proved that Adaline algorithm converges for any and all boolean functions
        total_MSE = 0
        for i in range(len(trainSet)):
            w1_old = w1_new
            w2_old = w2_new
            b_old = b_new
            x1 = trainSet[i][0]
            x2 = trainSet[i][1]
            t = ansTrainSet[i]

            yIn = b_old + (w1_old * x1) + (w2_old * x2)
            if t - yIn != 0:
                # Update the weights if MSE != 0
                w1_new = w1_old + (learningRate * (t - yIn) * x1)
                w2_new = w2_old + (learningRate * (t - yIn) * x2)
                b_new = b_old + (learningRate * (t - yIn))

                # # Compute deltas
                # delta_w1 = w1_new - w1_old
                # delta_w2 = w2_new - w2_old
                # delta_b = b_new - b_old

                MSE = (t - yIn) ** 2
                total_MSE += MSE
                print("w1: ", str(w1_new), " w2: ", str(w2_new), "b: ", str(b_new), "MSE: ", MSE, "TotalMSE: ", total_MSE/len(trainSet))
    return w1_new, w2_new, b_new


def AdalineTest(testSet, ansTestSet, w1, w2, b):
    """
    function check the parameters we got from Adaline algorithm on new data
    :param testSet:
    :param ansTestSet:
    :param w1: as found in Adaline function
    :param w2: as found in Adaline function
    :param b: as found in Adaline function
    :return:
    """
    testSet = np.array(testSet)
    testSet /= 100
    ansLst = []
    for i in range(len(testSet)):
        # for each element in testSet we will compute yIn with the given values, according to the formula:
        # yIn = b_old + (w1_old * x1) + (w2_old * x2)
        ansLst.append(b + (w1 * testSet[i][0]) + (w2 * testSet[i][1]))
    ansLst = np.array(ansLst)
    ansLst = np.round(ansLst)
    ansLst[ansLst > 1] = 1
    ansLst[ansLst <= 1] = -1
    print("accuracy_score", accuracy_score(ansTestSet, ansLst))
    return ansLst


def MSEFunc(a: np.ndarray, b: np.ndarray) -> float:
    return np.square(a - b).mean()


def main():
    trainSet, ansTrainSet = randomGenerator()
    testSet, ansTestSet = randomGenerator()

    # trainSet = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # ansTrainSet = [-1, 1, -1, -1]
    w1, w2, b = adaline(trainSet, ansTrainSet)
    AdalineTest(testSet, ansTestSet, w1, w2, b)


if __name__ == '__main__':
    main()
