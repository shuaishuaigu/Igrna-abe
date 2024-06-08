import matplotlib.pyplot as plt
import keras
import pandas as pd
import numpy as np
import sys
from generate import generate
from embeding import embeding


import scipy
import scipy.stats
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten, Dropout
from keras.layers.convolutional import Convolution2D,Convolution1D,MaxPooling1D,AveragePooling1D
from tensorflow.keras.optimizers import Adam
# import theano
# import random
# import os
# import pickle
# import heapq
from tensorflow.keras.utils import to_categorical

def predict_site_eff(n20):
    # Input the n20 sequence to generate all changes in 2-9 bits of IgRNA DataFrane
    dt = generate(n20)

    print(dt)
    # All igrnas are embedded with the input N20 sequence return sequence vector martix
    X, Y, total_width = embeding(dt, 'N20', 'gn20', 'F')
    # np.shape(X) ==> (1, 4, 23) == input shape


    # Value and process Y simultaneously
    yl = [y - 2 for y in Y]
    # one-hot embeding the value of Y
    yl = to_categorical(yl)
    # load model MES and SBE structure and weights

    # MES model
    site = keras.models.model_from_json(open('./site/model_arch.json').read())
    site.load_weights('./site/model_weights.h5')
    # site.compile(loss='categorical_crossentropy', optimizer='adam')

    # SBE model
    efficiency = keras.models.model_from_json(open('./rate/11.10-12.00-model_arch.json').read())
    efficiency.load_weights('./rate/11.10-12.00-model_weights.h5')
    # efficiency.compile(loss='mean_squared_error', optimizer='adam')

    print("load model success")

    # predict site
    Y_site_pred = site.predict(X,verbose=1)
    top_site_list = []
    # predict after combine each igrna and n20 top locus
    for y in Y_site_pred:
        site_prediction = y.argmax()
        top_site_list.append(site_prediction)

    # predict efficiency
    Y_pred = efficiency.predict(X, verbose=1)
    # reshape to  (65,)
    Y_pred = Y_pred.reshape(-1)  
    
    # ndarray transform to list type
   
    dictionnary = {
        "mismatch": dt['gn20'],
        "predict_rate": Y_pred,
        'predict_locus':top_site_list
    }
    # create DataFrame and select top 5 efficiency
    df_rate = pd.DataFrame(dictionnary)
    df_rate = df_rate.sort_values(by='predict_rate',ascending=False)
    # print(df_rate.head())
    # df_rate.sort_values(by='predict_rate', ascending=False, inplace=True)
    # df_rate.set_index('mismatch', inplace=True)
    # res = df_rate.head(5).to_dict()
    return df_rate.head()
   


if __name__ == '__main__':
    # test
    n20 = sys.argv[1]
    # After inputting N20, start generating all 2-9 igRNAs and perform optimal editing site prediction and efficiency prediction
    dd_content = predict_site_eff(n20)
    # print top 5 igrna sequences and predict their best editing site and efficiency
    print('The top five optimal IgRNAs, their efficiency, and the best editing sites')
    print('==============================================================')    
    print(dd_content)
    print('==============================================================')    
    print('Finally,If you want to predict their off target situation, you can connect to http://www.rgenome.net/cas-offinder/')
     