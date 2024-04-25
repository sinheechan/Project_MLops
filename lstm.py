# 주식 데이터를 사용하여 LSTM을 활용한 시계열 예측 모델을 구축

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
import datetime
import api_test_db

# external test

'''
data = api_test.df
data.head()
'''

# DB test

start = api_test_db.DBtest() # start 
print(start, type(start))
df = pd.read_csv('C:\sinheechan.github.io-master\Project_MLops\collect_files\data_from_db.csv')
data = pd.DataFrame(df)
print(data.head())

# 평균값을 계산한다. => 이후 주식 예측 값 예측

high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

# 윈도우 생성 => 최근 50일을 기준으로 함
seq_len = 50
sequence_length = seq_len + 1

result = []
for index in range(len(mid_prices) - sequence_length):
    result.append(mid_prices[index: index + sequence_length])

# 데이터 Normalization(정규화)
normalized_data = []
for window in result:
    normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

# train / test data 분할
row = int(round(result.shape[0] * 0.9))
train = result[:row, :]
np.random.shuffle(train)

x_train = train[:, :-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]

print(x_train.shape, x_test.shape)

# 모델 생성
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(5, activation='linear')) # output 다음날 하루
model.compile(loss='mse', optimizer='rmsprop')
model.summary()

# 훈련
model.fit(x_train, y_train,
    validation_data=(x_test, y_test),
    batch_size=10,
    epochs=20)

# 모델 저장
filename = datetime.datetime.now().strftime("%Y%m%d_%H%m%S")
model.save(filename + '_my_model.h5')

# 예측 수행
pred = model.predict(x_test)
fig = plt.figure(facecolor='white', figsize=(20, 10))
ax = fig.add_subplot(111)
ax.plot(y_test, label='True')
ax.plot(pred, label='Prediction')
ax.legend()
plt.savefig(filename + '_result.jpg', format='jpeg')
plt.show()