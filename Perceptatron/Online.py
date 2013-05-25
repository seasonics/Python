import math
import numpy as np
threshold = 0
learning_rate = .001
weights =  [0] * 784
training_set = []
i = 0


import time

def readIn (f):
    for line in f:
        var1 = line.split()
        for index, item in enumerate(var1):
            var1[index] = int(item)
        return tuple(var1)
    
def readInLabel(f):
    label_list = []
    buf = 0
    for line in f:
        if int(line) == 1:
            label_list.append(1)
        else:
            label_list.append(0)
    return label_list
                

f = open('stuff.txt', 'r')
f2 = open('label.txt', 'r')
label = readInLabel(f2)
while i<2000:
 list1 = []
 list2 = []
 list1 = readIn(f)
 val1 = label[i]
 list2.append(list1)
 list2.append(val1) 
 training_set.append(tuple(list2))
 i = i+1



    
#def readAndZip (f):
    #f = open(f, 'r')
    #for line in 

def lin_kern(x, y, sigma=5.0):
    #return np.exp(-linalg.norm(x-y)**2 / (2 * (sigma ** 2)))
    return np.dot(x, y)
def gaussian_kern(x, y):
    return np.exp(-(((np.linalg.norm(x-y))**2) / (2 * (5.3 ** 2))))


def linPerceptOnline (training_set):

    error_count = 0
    i = 0
    for input_vector, desired_output in training_set:
        result = np.dot(weights,input_vector) >= threshold
        error = desired_output - result
        if error != 0:
            error_count += 1
            for index, value in enumerate(input_vector):
                weights[index] += error * value
            print str(i) + ' ' + str(error_count)
        i = i+1
 
   

def kernOnline(training_set):

    s = [0] * 2200
    klist =[]
    for input_vector, desired_output in training_set:
        klist.append(list(input_vector))
    

    i = 0
    error_count = 0
    for input_vector, desired_output in training_set:
        if i == 0:
            result = (s[i] * gaussian_kern(np.array(input_vector),np.array(input_vector)))
            result = result >= threshold 
        else:
            j = 0
            while j < i+1:
                if s[j] != 0:
                    result = result+(float(s[j] * gaussian_kern(np.array(klist[j]),np.array(input_vector))))
                j = j+1
            result = result >= threshold
        if result == True:
            predict = 1
        else:
            predict = 0
        if (predict == 0 and desired_output == 1):
            s[i] = 1
            error_count = error_count+1
            print str(i) + ' ' + str(error_count)
        if (predict == 1 and desired_output == 0):
            s[i] = -1
            error_count = error_count+1
            print str(i) + ' ' + str(error_count)
        i = i+1
        result = 0

    
        
linPerceptOnline(training_set)
kernOnline(training_set)

