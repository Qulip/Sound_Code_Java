# -*- coding: utf8 -*-

import numpy as np

def remove_zero(sound_data):
    update_sound_data = []
    for i in range(len(sound_data)):
        if sound_data[i][1] != 0:
            update_sound_data.append(sound_data[i])

    return update_sound_data

def make_data(data):
    a = []
    for j, row in enumerate(data):
        if (j + 100 == len(data)):
            a = np.array(a)
            return a
        a.append(data[j:j + 100])
