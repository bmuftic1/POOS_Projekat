import random
import math
import numpy

def Euclidean(a, b):
    sum = .0
    for i in range(0, len(a) - 1):
        sum += math.pow((a[i] - b[i]), 2)
    return math.sqrt(sum)


def compareLists(l1, l2):
    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

def kMeansClustering(matrix, noOfClasses, outlierPercentage, maxNoOfIterations):
    means = []
    # initialize clusters randomly
    for i in range(0, noOfClasses):
        randomNumber = random.randint(0, len(matrix) - 1)
        if random in means:
            continue
        means.append(randomNumber)
    noOfIterations = 0
    while True:
        changeHappened = False
        clusters = []
        for i in range(0, noOfClasses):
            clusters.append([])
        # assign every element to a cluster (criterion: minimum Euclidean distance from cluster)
        for i in range(0, len(matrix)):
            distances = []
            for j in range(0, len(means)):
                distances.append(Euclidean(matrix[i], matrix[means[j]]))
            matrix[i][7] = numpy.argmin(distances) + 1
            clusters[numpy.argmin(distances)].append(matrix[i])
        # make new clusters as centroids of assigned clusters (and check for convergence)
        for i in range(0, noOfClasses):
            clusters[i].sort(key = lambda x : (x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
            if len(clusters[i]) > 0 and not compareLists(matrix[means[i]][0:7], clusters[i][int(len(clusters[i]) / 2)][0:7]):
                for j in range(0, len(matrix)):
                    if compareLists(matrix[j], clusters[i][int(len(clusters[i]) / 2)]):
                        means[i] = j
                        changeHappened = True
                        break
        if not changeHappened or noOfIterations == maxNoOfIterations:
            # delete outliers
            noOfOutlier = int(outlierPercentage * len(matrix))
            for i in range(0, noOfClasses):
                if len(clusters[i]) < noOfOutlier:
                    for j in range(0, len(clusters[i])):
                        for k in range(0, len(matrix)):
                            if k == len(matrix):
                                break
                            if compareLists(clusters[i][j], matrix[k]):
                                matrix.pop(k)
                    clusters[i].clear()
            break
        noOfIterations += 1
    return (matrix, clusters)


train = numpy.loadtxt(open("..\DeskriptorTrain.csv", "rb"), delimiter = ",", skiprows = 1).tolist()
# 2nd parameter: number of clusters, 3rd parameter: percentage for removal, 4th parameter: maximum number of iterations
(train, clusters) = kMeansClustering(train, 3, 0.1, 1000)
numpy.savetxt("..\DeskriptorClusteringTrain.csv", train, delimiter = ",", fmt="%11f")
for i in range(0, len(clusters)):
    print(len(clusters[i]))