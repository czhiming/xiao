#-*- coding:utf8 -*-
'''
Created on 17-11-2

@author: czm
'''
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import euclidean_distances
import numpy
import copy

New1 = [7.15759545085, 6.03899268887, 49.9000812348, 9.8878960195, 16291.2729488, -15.0979767985]
New2 = [15.234305924, 9.59858532272, 121.75596817, 30.2917771883, 1659.98143236, -36.0933122184]
New3 = [19.3440298507, 11.3126865672, 150.07761194, 41.9470149254, 940.856716418, -48.1415551866]
New4 = [26.7983870968, 13.3400537634, 190.337365591, 68.4919354839, 390.897849462, -70.4253669153]

def get_feature(feature_file):
    data = []
    for lines in open(feature_file):
        lines = lines.strip().split('\t')
        lines = map(lambda x:float(x),lines)
        data.append(lines)
    return data

def get_file(file_name):
    data = []
    for lines in open(file_name):
        lines = lines.strip()
        data.append(lines)
    return data


bnc_features = get_feature('bnc/bnc.large.txt.tok.features')
bnc = get_file('bnc/bnc.large.txt.remove')

X = copy.copy(bnc_features)
X.append(New1)
X.append(New2)
X.append(New3)
X.append(New4)

X = preprocessing.scale(X)

New = {0:[],1:[],2:[],3:[]}
for i in range(len(bnc_features)):

    cosine = numpy.array([euclidean_distances(X[i].reshape(1,-1), X[-4].reshape(1,-1)),
                          euclidean_distances(X[i].reshape(1,-1), X[-3].reshape(1,-1)),
                          euclidean_distances(X[i].reshape(1,-1), X[-2].reshape(1,-1)),
                          euclidean_distances(X[i].reshape(1,-1), X[-1].reshape(1,-1))])
    idx = numpy.argmin(cosine)
    New[idx].append(bnc[i])

with open('select_new1.bnc.txt','w') as fp:
    for lines in New[0]:
        fp.writelines(lines+"\n")

with open('select_new2.bnc.txt','w') as fp:
    for lines in New[1]:
        fp.writelines(lines+"\n")

with open('select_new3.bnc.txt','w') as fp:
    for lines in New[2]:
        fp.writelines(lines+"\n")

with open('select_new4.bnc.txt', 'w') as fp:
    for lines in New[3]:
        fp.writelines(lines + "\n")






























if __name__ == '__main__':
    pass
