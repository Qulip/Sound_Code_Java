# -*- coding: utf8 -*-

import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])
install("speechRecognition")
import speech_recognition as sr
from difflib import SequenceMatcher
import random
#  static
r = sr.Recognizer()
keySet = ["안녕하세요 2차 인증 테스트 입니다",
          "파이썬과 자바",
          "애플과 갤럭시",
          "노트북 컴퓨터 키보드 마우스",
          "책상에서 공부하는 학생"]
rating_scale = 0.8



def recognize_kor(wav_file):
    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)
    #     try except 해서 예외처리 해야할듯...!
    # return r.recognize_google(audio, language='ko', show_all=True)
    return r.recognize_google(audio, language='ko')

def calculate_result(result):
    print(result)
    ratio = SequenceMatcher(None, result, key).ratio()
    print("유사성_ratio :" , ratio)
    if ratio >= rating_scale:
        return True, ratio
    return False, ratio


def execute_stt(wav_file):
    return calculate_result(recognize_kor(wav_file))


def choice_key():
    return random.choice(keySet)

def show_key_index():
    global key
    key = choice_key()
    return keySet.index(key)

