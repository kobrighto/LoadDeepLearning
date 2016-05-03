'''An implementation of sequence to sequence learning for performing addition
Input: "535+61"
Output: "596"
Padding is handled by using a repeated sentinel character (space)
Input may optionally be inverted, shown to increase performance in many tasks in:
"Learning to Execute"
http://arxiv.org/abs/1410.4615
and
"Sequence to Sequence Learning with Neural Networks"
http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf
Theoretically it introduces shorter term dependencies between source and target.
Two digits inverted:
+ One layer LSTM (128 HN), 5k training examples = 99% train/test accuracy in 55 epochs
Three digits inverted:
+ One layer LSTM (128 HN), 50k training examples = 99% train/test accuracy in 100 epochs
Four digits inverted:
+ One layer LSTM (128 HN), 400k training examples = 99% train/test accuracy in 20 epochs
Five digits inverted:
+ One layer LSTM (128 HN), 550k training examples = 99% train/test accuracy in 30 epochs
'''

from __future__ import print_function
from keras.models import Sequential
#from keras.engine.training import slice_X
from keras.layers.core import Dense, Activation, TimeDistributedDense, RepeatVector
from keras.layers import recurrent
import numpy as np
import DataPostProcessing
import pandas as pd
#from six.moves import range


class CharacterTable(object):
    '''
    Given a set of characters:
    + Encode them to a one hot integer representation
    + Decode the one hot integer representation to their character output
    + Decode a vector of probabilties to their character output
    '''
    def __init__(self, chars, maxlen):
        self.chars = sorted(set(chars))
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))
        self.maxlen = maxlen

    def encode(self, C, maxlen=None):
        maxlen = maxlen if maxlen else self.maxlen
        X = np.zeros((maxlen, len(self.chars)))
        for i, c in enumerate(C):
            X[i, self.char_indices[c]] = 1
        return X

    def decode(self, X, calc_argmax=True):
        if calc_argmax:
            X = X.argmax(axis=-1)
        return ''.join(self.indices_char[x] for x in X)


class colors:
    ok = '\033[92m'
    fail = '\033[91m'
    close = '\033[0m'

# Parameters for the model and dataset
DIGITS = 3
# Choices: GRU, SimpleRNN, LSTM
RNN = recurrent.LSTM
HIDDEN_SIZE = 128
BATCH_SIZE = 128
LAYERS = 2
#MAXLEN = DIGITS + 1 + DIGITS
MAXLEN = DIGITS * 12
NB_EPOCHS = 200

chars = '0123456789'
ctable = CharacterTable(chars, MAXLEN)

#questions = []
#expected = []
#seen = set()
print('Generating data...')

cpuList, memList = DataPostProcessing.meanLoad(8107,30)
markPoint = int(0.9*len(cpuList))
trainList = cpuList[:markPoint]
testList = cpuList[markPoint:]
X_to_train,y_to_train = DataPostProcessing.makeListSequence(trainList=trainList,trainingStep=1,inputvector=(1,12)
                                                         ,labelvector=(1,6))
X_to_test,y_to_test = DataPostProcessing.makeListSequence(trainList=testList,trainingStep=1,inputvector=(1,12)
                                                       ,labelvector=(1,6))

print('Vectorization...')
X_train = np.zeros((len(X_to_train), MAXLEN, len(chars)), dtype=np.bool)
y_train = np.zeros((len(y_to_train), DIGITS*6, len(chars)), dtype=np.bool)

for i, sentence in enumerate(X_to_train):
    X_train[i] = ctable.encode(sentence, maxlen=MAXLEN)
for i, sentence in enumerate(y_to_train):
    y_train[i] = ctable.encode(sentence, maxlen=DIGITS*6)

X_test = np.zeros((len(X_to_test), MAXLEN, len(chars)), dtype=np.bool)
y_test = np.zeros((len(y_to_test), DIGITS*6, len(chars)), dtype=np.bool)

for i, sentence in enumerate(X_to_test):
    X_test[i] = ctable.encode(sentence, maxlen=MAXLEN)
for i, sentence in enumerate(y_to_test):
    y_test[i] = ctable.encode(sentence, maxlen=DIGITS*6)

print('Build model...')
model = Sequential()
# "Encode" the input sequence using an RNN, producing an output of HIDDEN_SIZE
# note: in a situation where your input sequences have a variable length,
# use input_shape=(None, nb_feature).
model.add(RNN(HIDDEN_SIZE, input_shape=(MAXLEN, len(chars))))
# For the decoder's input, we repeat the encoded input for each time step
model.add(RepeatVector(DIGITS*6))
# The decoder RNN could be multiple layers stacked or a single layer
for _ in range(LAYERS):
    model.add(RNN(HIDDEN_SIZE, return_sequences=True))

# For each of step of the output sequence, decide which character should be chosen
model.add(TimeDistributedDense(len(chars)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam')

predictions = []
realvalues = []

model.fit(X_train,y_train,batch_size=BATCH_SIZE,nb_epoch=NB_EPOCHS, show_accuracy=True,
          validation_data=(X_test,y_test))

for i in xrange(len(X_test)):
    rowX, rowy = X_test[np.array([i])], y_test[np.array([i])]

    preds = model.predict_classes(rowX,verbose=0)
    correct = ctable.decode(rowy[0])
    guess = ctable.decode(preds[0], calc_argmax=False)
    predictions.append(str(guess))
    realvalues.append(str(correct))

pd.DataFrame(predictions).to_csv("predicted_8107_20epochs.csv")
pd.DataFrame(realvalues).to_csv("test_data_8107_20epochs.csv")