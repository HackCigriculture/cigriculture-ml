import random
import time

from network import network
from polygon import check


model = network()
model.compile(optimizer='rmsprop',
              loss='mse',
              )

while True:
    train_x = []
    train_y = []
    for _i in range(1000):
        longitude = random.uniform(121, 122)
        latitude = random.uniform(24, 26)
        train_x.append([longitude - 121.0, (latitude - 24.0) / 2.0])
        train_y.append([check(longitude, latitude)])
    model.fit(train_x,
              train_y,
              nb_epoch=1000,
              validation_split=0.2,
              )
    model.save_weights('model/' + str(int(time.time())) + '.result')
