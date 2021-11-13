import tensorflow as tf
from model.generate_data import load_wave_generator_file
from code.functions import make_data

print(tf.__version__)

model = tf.keras.models.load_model('2학기화자인식모델_유일권.h5')

data = load_wave_generator_file("일권.wav")
test_data = make_data(data)
result = model.predict(test_data[:10])

print(result)

