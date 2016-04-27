import pandas as pd
from random import random
from os import listdir, chdir, path
import platform
import DataPostProcessing
import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM

in_neurons = 3
out_neurons = 6
hidden_neurons = 100
nb_classes = 10

model = Sequential()
model.add(LSTM(output_dim=hidden_neurons, input_dim=in_neurons, return_sequences=False))
model.add(Dense(output_dim=out_neurons, input_dim=hidden_neurons))
model.add(Activation("linear"))
model.compile(loss="mean_squared_error", optimizer="rmsprop")

cpuList, memList = DataPostProcessing.meanLoad(8107,2)
X_train,y_train,X_test,y_test = DataPostProcessing.makeTrainTestList_seq(cpuList,0.9*6946,(15,3),(15,6))

print ('Evaluate seq2seqLSTM...')

model.fit(X_train, y_train, batch_size=5, nb_epoch=nb_classes, show_accuracy=True, verbose=1)

predicted = model.predict(X_test)

pd.DataFrame(predicted).to_csv("predicted.csv")
pd.DataFrame(y_test).to_csv("test_data.csv")

# and maybe plot it
#pd.DataFrame(y_test[:100]).plot("test_data.csv")