##### 화자인식 일반 머신러닝 코드 #####
import librosa
import librosa.display
# import pyaudio #마이크를 사용하기 위한 라이브러리
import wave
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

from model.generate_data import *
from code.functions import make_data

# 0 numbers directory files = user wav file
# noise_data : 50000 MFCC data
user = load_wave_generator("D:/코딩/자바/soundCode/python_server/data/sound_data/0")
noise = np.loadtxt("D:/코딩/자바/soundCode/python_server/data/noise_data.txt", delimiter=",")

# remove zero
user = remove_zero(user)

# make data_label
user_label = np.full(len(user), 0)
noise_label = np.full(len(noise), 1)


x_train = np.concatenate((user, noise), axis = 0)
y_train = np.concatenate((user_label, noise_label), axis = 0)

print(x_train.shape)
print(y_train.shape)


# SMOTE part
from imblearn.over_sampling import *

x_smote, y_smote = SMOTE().fit_resample(x_train, y_train)
rand_Idx = np.arange(x_smote.shape[0])
np.random.shuffle(rand_Idx)
x_smote = x_smote[rand_Idx]
y_smote = y_smote[rand_Idx]



from keras.models import Sequential
from keras import layers
from keras.layers import Dropout

model = Sequential()
model.add(layers.Dense(10000, input_shape=(45,), activation='relu'))
model.add(Dropout(0.3))
model.add(layers.Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(layers.Dense(32, activation='relu'))
model.add(Dropout(0.3))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'],
              )


history = model.fit(x_smote, y_smote, epochs=5, batch_size=512)

model.save('2학기화자인식모델_유저.h5')

print("save 완료!")
