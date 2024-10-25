# 주식 데이터를 사용하여 LSTM을 활용한 시계열 예측 모델을 구축

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
import datetime
import os

# 데이터 불러오기
directory = r'C:/sinheechan.github.io-master/Project_MLops/db_to_df'
files = os.listdir(directory)

if files:  # 파일이 존재할 경우
    sorted_file = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True) # 파일들의 수정된 시간을 기준으로 정렬
    recent_file = sorted_file[0]  # 정렬된 목록에서 가장 첫 번째 파일이 최근에 업로드된 파일

    recent_file_path = os.path.join(directory, recent_file)
    data = pd.read_csv(recent_file_path)

    print("적용 파일 명:", recent_file)
    print(data.head())

else:
    print("디렉토리에 파일이 존재하지 않습니다.")

# 데이터 전처리
# 평균값을 계산 => 이후 주식 예측 값 예측
high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

# 기간
seq_len = 50  # 50일 기준
sequence_length = seq_len + 1

result = []
for index in range(len(mid_prices) - sequence_length):
    result.append(mid_prices[index: index + sequence_length])

# 데이터 정규화
normalized_data = []
for window in result:
    normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

# train / test data 분할
row = int(round(result.shape[0] * 0.9))
train = result[:row, :]
np.random.shuffle(train)  # 섞기

x_train = train[:, :-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]  # 마지막 값만 예측

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]

print(x_train.shape, x_test.shape)

# 모델 생성
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))  # 50일 기준으로 변경
model.add(LSTM(64, return_sequences=False))
model.add(Dense(1, activation='linear'))  # 단일 값 예측
model.compile(loss='mse', optimizer='rmsprop')
model.summary()

# 훈련
model.fit(x_train, y_train,
          validation_data=(x_test, y_test),
          batch_size=10,
          epochs=20)

# 모델 저장
save_model_dir = r'C:/sinheechan.github.io-master/Project_MLops/models'
filename = datetime.datetime.now().strftime("%Y%m%d_%H%m%S")
model_save = os.path.join(save_model_dir, filename + '_my_model.h5')

model.save(model_save)

# 예측 수행 / 시각화 그래프 저장
pred = model.predict(x_test)
fig = plt.figure(facecolor='white', figsize=(20, 10))
ax = fig.add_subplot(111)
ax.plot(y_test, label='실제')
ax.plot(pred, label='예측')
ax.legend()
ax.set_xlabel('시간(일)')
ax.set_ylabel('예측 주가')

# 예측 그래프 저장
save_map_dir = r'C:/sinheechan.github.io-master/Project_MLops/results'
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
image_save = os.path.join(save_map_dir, filename + '_result.jpg')

plt.savefig(image_save, format='jpeg')
plt.show()