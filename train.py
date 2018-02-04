#-*- coding:utf8 -*-
'''
Created on Dec 5, 2016

@author: czm
'''

import numpy
from numpy import var,std,mean
from sklearn.svm import SVR,SVC
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from scipy.stats import pearsonr,spearmanr,ttest_ind,ttest_rel
import json

def get_feature(feature_file):
    data = []
    for lines in open(feature_file):
        lines = lines.strip().split('\t')
        lines = map(lambda x:float(x),lines)
        data.append(lines)
    return numpy.array(data)

def get_label(label_file):
    hter = []
    for lines in open(label_file):
        #print lines
        lines = float(lines.strip())
        hter.append(lines)
    return numpy.array(hter)

X = get_feature('bnc/bnc.txt.features')
y = get_label('bnc/bnc.2000.mean.txt.label')
#归一化
X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

svr = SVR()

#gridSearch调参数
parameters = {'kernel':['linear','rbf'],'C':[0.01,1.,10.],'epsilon':[0.01,1.,10.]}
clf = GridSearchCV(svr,parameters,cv=5)
clf.fit(X_train, y_train)
#print clf.best_params_


svr.fit(X_train, y_train)
#print svr.score(X_test, y_test)
y_pred = clf.predict(X_test)

#result = numpy.hstack((X_test,y_pred[:,None],y_test[:,None]))[:10,:]
#print result
print pearsonr(y_pred, y_test)
print spearmanr(y_pred, y_test)
#print svr.coef_


results = []

X_test = get_feature('NewConcept/NewConcept_book1.txt.punkt.tok.features')
print mean(X_test[:,0])
print mean(X_test[:,1])
print mean(X_test[:,2])
print mean(X_test[:,3])
print mean(X_test[:,4])
print mean(X_test[:,5])
X_test = preprocessing.scale(X_test)
y_pred = clf.predict(X_test)
print 'NewConcept_book1.txt:',mean(y_pred) 
results.append(list(y_pred))

X_test = get_feature('NewConcept/NewConcept_book2.txt.punkt.tok.features')
print mean(X_test[:,0])
print mean(X_test[:,1])
print mean(X_test[:,2])
print mean(X_test[:,3])
print mean(X_test[:,4])
print mean(X_test[:,5])
X_test = preprocessing.scale(X_test)
y_pred = clf.predict(X_test)
print 'NewConcept_book2.txt:',mean(y_pred) 
results.append(list(y_pred))

X_test = get_feature('NewConcept/NewConcept_book3.txt.punkt.tok.features')
print mean(X_test[:,0])
print mean(X_test[:,1])
print mean(X_test[:,2])
print mean(X_test[:,3])
print mean(X_test[:,4])
print mean(X_test[:,5])
X_test = preprocessing.scale(X_test)
y_pred = clf.predict(X_test)
print 'NewConcept_book3.txt:',mean(y_pred) 

results.append(list(y_pred))

X_test = get_feature('NewConcept/NewConcept_book4.txt.punkt.tok.features')
print mean(X_test[:,0])
print mean(X_test[:,1])
print mean(X_test[:,2])
print mean(X_test[:,3])
print mean(X_test[:,4])
print mean(X_test[:,5])
X_test = preprocessing.scale(X_test)
y_pred = clf.predict(X_test)
print 'NewConcept_book4.txt:',mean(y_pred) 
results.append(list(y_pred))

with open('data.json','w') as fp:
    json.dump(results,fp)





