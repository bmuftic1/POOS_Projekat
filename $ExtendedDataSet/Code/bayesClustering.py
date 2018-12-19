import csv
import numpy as np
import pandas as pd
import math
import os as os
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB

os.chdir('..')

train = pd.read_csv('./DeskriptorClusteringTrain.csv').as_matrix()
outcome = train[:,7]
train = train[:,0:7]

test = pd.read_csv('./DeskriptorTest.csv').as_matrix()
test=test.reshape(21,7)

model = GaussianNB()
model.fit(train, outcome)
predicted = model.predict(test)

truth = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3]

acc = accuracy_score(predicted, truth)
print("Accuracy sa accuracy_score za citav model (Gaussian bez priors): {}\n".format(acc))

model = GaussianNB(priors=[0.9, 0.05, 0.05])
model.fit(train, outcome)
predicted = model.predict(test)

acc = accuracy_score(predicted, truth)
print("Accuracy sa accuracy_score za citav model (Gaussian sa priors): {}\n".format(acc))


model = BernoulliNB()
model.fit(train, outcome)
pred = model.predict(test)


acc = accuracy_score(pred, truth)
print("Accuracy sa accuracy_score za citav model (Bernoulli): {}\n".format(acc))


confusionMatrix = [[0,0,0], [0,0,0],[0,0,0]]

for i in range(0, len(truth)):
	indeks = int(i/7)
	if(truth[i]==predicted[i]):
		confusionMatrix[indeks][indeks]+=1
	else:
		confusionMatrix[indeks][int(predicted[i]-1)]+=1

#uzor: https://www.researchgate.net/post/Can_someone_help_me_to_calculate_accuracy_sensitivity_of_a_66_confusion_matrix

print("\nConfusion matrix:")
for i in range(0,3):
	print(confusionMatrix[i])
print("")

print("\nKlasa 1")
TP = confusionMatrix[0][0]
TN = confusionMatrix[1][1] + confusionMatrix[2][2]
zbir = TP + TN
FP = confusionMatrix[1][0]+confusionMatrix[2][0]
FN = confusionMatrix[0][1]+confusionMatrix[0][2]
print("Acc: {}".format(float(TP+TN)/21))
print("Sen: {}".format(float(TP)/(TP+FN)))
print("Spec: {}".format(float(TN)/(TN+FP)))
print("")

print("\nKlasa 2")
TP = confusionMatrix[1][1]
TN = confusionMatrix[0][0] + confusionMatrix[2][2]
zbir = TP + TN
FP = confusionMatrix[0][1]+confusionMatrix[2][1]
FN = confusionMatrix[1][0]+confusionMatrix[1][2]
print("Acc: {}".format(float(TP+TN)/21))
print("Sen: {}".format(float(TP)/(TP+FN)))
print("Spec: {}".format(float(TN)/(TN+FP)))
print("")

print("\nKlasa 3")
TP = confusionMatrix[2][2]
TN = confusionMatrix[0][0] + confusionMatrix[1][1]
zbir = TP + TN
FP = confusionMatrix[0][2]+confusionMatrix[1][2]
FN = confusionMatrix[2][0]+confusionMatrix[2][1]
print("Acc: {}".format(float(TP+TN)/21))
print("Sen: {}".format(float(TP)/(TP+FN)))
print("Spec: {}".format(float(TN)/(TN+FP)))
print("")