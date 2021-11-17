##### 화자인식 일반 머신러닝 코드 #####
import librosa
import librosa.display
# import pyaudio #마이크를 사용하기 위한 라이브러리
import wave
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from imblearn.over_sampling import *
from model.generate_data import *
from function.functions import make_data


chang = load_wave_generator("D:/코딩/자바/soundCode/python_server/data/sound_data/0")
jae = load_wave_generator("D:/코딩/자바/soundCode/python_server/data/sound_data/1")
# yu = load_wave_generator("D:/코딩/자바/soundCode/python_server/data/sound_data/2")
yu = load_wave_generator_file("일권.wav")


chang_label = np.full(len(chang), 1)
jae_label = np.full(len(jae), 1)
yu_label = np.full(len(yu), 0)

x_train = np.concatenate((chang, jae, yu), axis = 0)
y_train = np.concatenate((yu_label, jae_label, chang_label), axis = 0)

print(len(chang) + len(jae))


x_train, y_train = SMOTE().fit_resample(x_train, y_train)

chang_gru = make_data(chang)
jae_gru = make_data(jae)
yu_gru = make_data(yu)

chang_label = np.full(len(chang_gru), 1)
jae_label = np.full(len(jae_gru), 1)
yu_label = np.full(len(yu_gru), 0)

x_train = np.concatenate((yu_gru, jae_gru, chang_gru), axis = 0)
y_train = np.concatenate((yu_label, jae_label, chang_label), axis = 0)

print(x_train.shape)
print(y_train.shape)





train = x_train
train_label = y_train


from keras.models import Sequential
from keras import layers

model = Sequential()
model.add(layers.GRU(128, input_shape=(100, 45)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'],
              )


history = model.fit(train, train_label, epochs=2, batch_size=512)

model.save('2학기화자인식모델_유일권.h5')

print("save 완료!")
