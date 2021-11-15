# -*- coding: utf8 -*-

# print(sys.path)
from function.stt import *
from function.recognize import *

# 1
# 어떤 key값으로 할건지 (일정하지 않다면 어떻게 ?)
# 많이 만들어 놓고 랜덤하게 전달하고 그 랜덤 값이 맞는지 체크!
# 그렇다면 크롤링이나 제작자 조차 알 수 없게끔 만드는 건 어떨까 ( 보안 )

# 2
# 맞다고 할 기준 설정 어떻게?

# 3
# 속도 좀 느린데 내 컴퓨터라서 그럴수도 있음

# 4
# 음성 어떻게 받아올까?

# 5
# 학습 해야함
# 회원가입 시 모델학습

# 6
# 보관은 어디에?

def execute(wav_file_name):
    wav_file = "D:\\코딩\\자바\\soundCode\\python_server\\data\\" + wav_file_name + ".wav"
    reg_flag, reg_similarity = execute_recognize(wav_file)
    stt_flag, stt_similarity = execute_stt(wav_file)
    list = []

    if reg_flag and stt_flag:
        list.append(True)
        list.append(reg_similarity)
        list.append(stt_similarity)
        return list
    list.append(False)
    list.append(reg_similarity)
    list.append(stt_similarity)
    return list


# print(execute("D__코딩_자바_soundCode_data_changJun (2)"))