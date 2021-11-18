# -*- coding: utf8 -*-


# from keras.models import load_model
import tensorflow as tf
import librosa
from function.functions import *

print(tf.__version__)
#  static
# model = tf.keras.models.load_model('D:/코딩/자바/soundCode/python_server/data/userModel/user.h5')
rating_scale = 0.5
right_standard = 0.9
wrong_standard = 0.2

def sound_to_test_data(wav_file):
    y, sr = librosa.load(wav_file)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=45, hop_length=int(sr*0.01), n_fft=int(sr*0.02)).T
    update_mfcc = remove_zero(mfcc)
    return np.array(update_mfcc)


def model_result(final_mfcc):
    model = tf.keras.models.load_model('D:/코딩/자바/soundCode/python_server/data/userModel/user.h5')
    y_pred = model.predict(final_mfcc)
    zero_count = 0

    for i in y_pred:
        if i < 0.5:
            zero_count += 1

    return zero_count/len(y_pred)

def calculate_result(zero_percentage):
    print("zero_percentage :" , zero_percentage)
    if zero_percentage >= right_standard:
        return True, zero_percentage
    return False, zero_percentage


def execute_recognize(wav_file):
    final_mfcc = sound_to_test_data(wav_file)
    zero_percentage = model_result(final_mfcc)
    return calculate_result(zero_percentage)

# wav_file = "D:\\코딩\\자바\\soundCode\\python_server\\data\\" + "감자고구마.wav"
# execute_recognize(wav_file)
