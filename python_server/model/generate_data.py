import librosa
import librosa.display
# import pyaudio #마이크를 사용하기 위한 라이브러리
import wave
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def load_wave_generator_file(wav):
    path = "D:/코딩/자바/soundCode/python_server/data"
    y, sr = librosa.load(path + "/" + wav)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=45, hop_length=int(sr * 0.01),
                                n_fft=int(sr * 0.02)).T
    data_mfcc = []

    if len(data_mfcc) == 0:
        data_mfcc = mfcc
    else:
        data_mfcc = np.concatenate((data_mfcc, mfcc), axis=0)

    update_data_mfcc = []

    for i in range(len(data_mfcc)):
        if data_mfcc[i][1] != 0:
            update_data_mfcc.append(data_mfcc[i])

    return np.array(update_data_mfcc)


def load_wave_generator(path):
    if not os.path.isdir(path):
        print("폴더가 아닙니다!")
        return
    files = os.listdir(path)

    print("Foldername :", path, ", - file count : ", len(files))  # 폴더 이름과 그 폴더에 속하는 파일 갯수 출력
    data_mfcc = []
    data_label = []
    for wav in files:
        if not wav.endswith(".wav"):
            continue
        else:
            print("Filename :", wav)  # .wav 파일이 아니면 continue
            y, sr = librosa.load(path + "/" + wav)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=45, hop_length=int(sr * 0.01),
                                        n_fft=int(sr * 0.02)).T

            if len(data_mfcc) == 0:
                data_mfcc = mfcc

            else:
                data_mfcc = np.concatenate((data_mfcc, mfcc), axis=0)

    update_data_mfcc = []

    for i in range(len(data_mfcc)):
        if data_mfcc[i][1] != 0:
            update_data_mfcc.append(data_mfcc[i])

    return np.array(update_data_mfcc)

