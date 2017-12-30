# -*- coding: utf-8 -*-
import random
import numpy as np
import json
import time as t
from scipy import sparse, io
from sklearn import metrics
from sklearn.externals import joblib
import sklearn.feature_extraction.text
from sklearn.linear_model import LogisticRegression
from initial_tfidf import create_word_vec
from data_import import load_data
import sys

#构造LR预测类
class Logistic_Predictor:
    #load 持久化模型
    clf = joblib.load(sys.path[0].replace('\\','/')+'/model/logistic_estimator.pkl')
    vector_tfidf = joblib.load(sys.path[0].replace('\\','/')+'/model/tf_idf.pkl')

    def __init__(self, test_data, test_label):
        self.test_data = self.vector_tfidf.transform(test_data)
        self.test_label = test_label
    #重置测试数据
    def reset_data(self, test_data, test_label):
        self.test_data = self.vector_tfidf.transform(test_data)
        self.test_label = test_label
    #预测，打印矩阵
    def predict(self):
        test_result = self.clf.predict(self.test_data)
        print (metrics.classification_report(self.test_label, test_result, digits = 5))
        print (metrics.confusion_matrix(self.test_label, test_result))
    
    #预测，返回概率。return list.
    def predict_proba(self):
        result = self.clf.predict_proba(self.test_data)
        result = np.round(result, 2)
        num = result.shape[0]
        return result

if '__main__' == __name__:
    t0 = t.time()
    #test
    print("start predict:")
    test_data, test_label = load_data(sys.path[0].replace('\\','/')+'/datas/test_data.txt')
    print(len(test_data))

    #predict data
    predictor = Logistic_Predictor(test_data, test_label)
    predictor.predict()
    predictor.predict_proba()
    
    #reset data
    predictor.reset_data(test_data[:10], test_label[:10])
    predictor.predict()
    predictor.predict_proba()

    print("predicting time: %0.3fs" % (t.time() - t0))
