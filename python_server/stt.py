# -*- coding: utf8 -*-

import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])
install("speechRecognition")
import speech_recognition as sr
from difflib import SequenceMatcher

#  static
r = sr.Recognizer()
key = "안녕하세요 감자 고구마 테스트 입니다"
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




