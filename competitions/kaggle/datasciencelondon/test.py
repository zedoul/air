# -*- coding: utf-8 -*-
"""
Created on Wed Apr 02 11:47:58 2014
@author: gsubramanian
"""

import pylab as pl
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split,StratifiedKFold,cross_val_score
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFECV
from sklearn.svm import SVC
import sklearn.preprocessing as pp

############################## Read data ###################################################

working_directory ="./data/"

train_init = np.genfromtxt(open(working_directory + 'train.csv','rb'), delimiter=',')
target_init = np.genfromtxt(open(working_directory + 'trainLabels.csv','rb'), delimiter=',')
test_init = np.genfromtxt(open(working_directory + 'test.csv','rb'), delimiter=',')

############################################################################################

"""
Split data into train and test
"""
def dsplit(train_init,target_init):
    train,test,train_target,test_target = train_test_split(train_init,target_init,test_size=0.1,random_state=42)
    return train,test,train_target,test_target

def stratk(train_init,target_init):
    sk = StratifiedKFold(target_init,n_folds=2)
    
    for train_index,test_index in sk:
        train = train_init[train_index]
        test  = train_init[test_index]
        train_target = target_init[train_index]
        test_target = target_init[test_index]
    return train,test,train_target,test_target

(instances,features) = train_init.shape


"""
Plot the raw variables as scatter
color by class label
"""
def rawPlot(train_init,target_init):
   for i in range(0,features):
        for j in range(0,features):
            #pl.figure(i+1)
            pl.scatter(train_init[:,i],train_init[:,j],c=target_init)
            pl.xlabel(i)
            pl.ylabel(j)
            pl.savefig(working_directory + 'images/img_' + str(i) + '_' + str(j) + '.jpeg')
            print i,j
   pl.show()



"""
Nearest neighbour classifier
"""
def classifier(train,test,train_target,test_target):

    
    kclass = KNeighborsClassifier(n_neighbors=13,algorithm='kd_tree',weights='uniform',p=1)
    kclass.fit(train,train_target)
    res = kclass.predict(train)
    
    print classification_report(train_target,res)
    
    res1 = kclass.predict(test)
    print classification_report(test_target,res1)
    return kclass
 
"""
Feature selection
"""
def optimalFeatures(train,target):
    sk = StratifiedKFold(target,n_folds=3)
    est = SVC(kernel='linear')
    rfecv = RFECV(est,cv=sk)
    rfecv.fit(train,target)
    print("Optimal number of features : %d" % rfecv.n_features_)
    
    
    return rfecv

"""
perform pca
"""
def dopca(train,train_target,test,test_init):
    pca = PCA(n_components=12,whiten=True)
    train = pca.fit_transform(train,train_target)
    test = pca.transform(test)
    test_init =pca.transform(test_init)
    return train,test,test_init
    

def minmax(train,test):
    mmax= pp.MinMaxScaler()
    train = mmax.fit_transform(train)
    test = mmax.transform(test)
    return train,test
    
def norm(train,test):
    norm = pp.Normalizer()
    train = norm.fit_transform(train)
    test = norm.transform(test)
    return train,test
    

train,test,train_target,test_target = dsplit(train_init,target_init)
#train,test,train_target,test_target = stratk(train_init,target_init)

#train,test = norm(train,test)
#train,test_init = norm(train,test_init)
#train,test = minmax(train,test)
#train,test_init = minmax(train,test_init)

#rfecv = optimalFeatures(train,train_target)
#train = rfecv.transform(train)
#test = rfecv.transform(test)
#test_init=rfecv.transform(test_init)

train,test,test_init = dopca(train,train_target,test,test_init)


est =classifier(train,test,train_target,test_target)




res = est.predict(test_init)
idcol = np.arange(start=1,stop=9001)
res2 = np.column_stack((idcol,res))

np.savetxt(working_directory + 'prediction.csv',res2,fmt='%d',delimiter=",")


