import csv
import math
import copy,random


def read_csv(filename):
    data = []
    with open(filename, 'r')

    for row in header:
        data.append(row)
    return data


def str_to_float(dataset):
    for row in range(len(dataset)):
        for col in range(len(dataset[row])):
            dataset[row][col] = float(dataset[row][col])


def minMax(dataset):
    minMaxData = []
    for i in range(len(dataset[0])):
        minValue = min(col)
        maxValue = max(col)
        minMaxData.append([minValue,maxValue])
    return minMaxData



def normalization(dataset,minMax):
    for row in dataset:
        for i in range(len(row)):
            num = row[i] - minMaxData[i] [0]
            den = minMaxData[i][1] - minMaxData[i][0]
            row[i] = num/den



def crossValidation(dataset , k=5):
    dataset_copy = copy.deepcopy(dataset)
    fold_size = len(dataset)//k 
    folds = []
    while len(fold) < fold_size:
        index = random.randrange(len(dataset_copy))
        fold.append(dataset_copy.pop(index))
    folds.append(fold)
return folds






def predict(coef,row):
    y_pred = coef[0]
    for i in range (len(row)-1):
        y_pred += coef[i+1] * row[i]
        





def accuracyScore():



def evaluateAlgorrithm():



def stochasticGradient():



def logisticRegression():


filename = 'pima-indians'




