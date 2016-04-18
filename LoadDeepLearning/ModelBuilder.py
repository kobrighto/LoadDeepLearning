from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.initializations import normal, identity
from keras.layers.recurrent import SimpleRNN, LSTM
from keras.optimizers import RMSprop
from keras.utils import np_utils


batch_size = 5
nb_classes = 2
nb_epochs = 200
hidden_units = 100

learning_rate = 1e-6
clip_norm = 1.0

woo = np.array([[1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]],np.int32)


# convert class vectors to binary class matrices
woo_label_raw = np.array([0,0,0,0,0,1,1,1,1,1],np.int32)
woo_label = np_utils.to_categorical(woo_label_raw, nb_classes)
#labels range from 0-999

#woo_label = np.array([1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1],np.int32)

new_woo = woo.reshape((10,4,1))
#reshape((number_of_data,30,1))
new_woo_label = woo_label.reshape(10,2)
#reshape((number_of_data,number_of_classes))
#number_of_classes = 1000 currently

new_woo_test = new_woo
new_woo_label_test = new_woo_label


print(new_woo)
print(new_woo_label)



print('Evaluate IRNN...')
model = Sequential()
model.add(SimpleRNN(output_dim=hidden_units,
                    init=lambda shape: normal(shape, scale=0.001),
                    inner_init=lambda shape: identity(shape, scale=1.0),
                    activation='relu', input_shape=new_woo.shape[1:]))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
rmsprop = RMSprop(lr=learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=rmsprop)

model.fit(new_woo, new_woo_label, batch_size=batch_size, nb_epoch=nb_epochs,
          show_accuracy=True, verbose=1, validation_data=(new_woo_test, new_woo_label_test))

scores = model.evaluate(new_woo_test, new_woo_label_test, show_accuracy=True, verbose=0)

print('IRNN test score:', scores[0])
print('IRNN test accuracy:', scores[1])

print('Compare to LSTM...')
model = Sequential()
model.add(LSTM(hidden_units, input_shape=new_woo.shape[1:]))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
rmsprop = RMSprop(lr=learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=rmsprop)

model.fit(new_woo, new_woo_label, batch_size=batch_size, nb_epoch=nb_epochs,
          show_accuracy=True, verbose=1, validation_data=(new_woo_test, new_woo_label_test))

scores = model.evaluate(new_woo_test, new_woo_label_test, show_accuracy=True, verbose=0)
print('LSTM test score:', scores[0])
print('LSTM test accuracy:', scores[1])
