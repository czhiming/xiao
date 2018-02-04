#-*- coding:utf8 -*-
'''
Created on 17-11-1

@author: czm
'''
import numpy
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.svm import SVR,SVC


def get_feature(feature_file):
    data = []
    for lines in open(feature_file):
        lines = lines.strip().split('\t')
        lines = map(lambda x:float(x),lines)
        data.append(lines)
    return numpy.array(data)

pca = PCA(n_components=2)

New1 = get_feature('NewConcept/NewConcept_book1.txt.punkt.tok.features')
New1 = preprocessing.scale(New1)
pca1 = pca.fit_transform(New1)

New2 = get_feature('NewConcept/NewConcept_book2.txt.punkt.tok.features')
New2 = preprocessing.scale(New2)
pca2 = pca.transform(New2)

New3 = get_feature('NewConcept/NewConcept_book3.txt.punkt.tok.features')
New3 = preprocessing.scale(New3)
pca3 = pca.transform(New3)

New4 = get_feature('NewConcept/NewConcept_book4.txt.punkt.tok.features')
New4 = preprocessing.scale(New4)
pca4 = pca.transform(New4)



fig, ax = plt.subplots()
ax.scatter(pca1[:,0], pca1[:,1], c='r',s=50, label='NewConcept1')
ax.scatter(pca2[:,0], pca2[:,1], c='g',s=50, label='NewConcept2')
ax.scatter(pca3[:,0], pca3[:,1], c='b',s=50, label='NewConcept3')
ax.scatter(pca4[:,0], pca4[:,1], c='y',s=50, label='NewConcept4')

ax.legend()
plt.show()









if __name__ == '__main__':
    pass