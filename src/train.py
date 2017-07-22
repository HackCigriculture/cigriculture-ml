import random
import time

from network import network
from polygon import check


model = network()
model.compile(optimizer='sgd',
              loss='mse',
              )

train_x = []
train_y = []
for _x in range(0, 100):
    for _y in range(0, 100):
        x = [_x / 100.0, _y / 100.0]
        longitude = _x / 1000.0 + 121.4539
        latitude = _y / 1000.0 + 24.9540
        y = check(longitude, latitude)
        if y == 1.0 and random.uniform(0, 1) > 0.0001:
            continue
        train_x.append(x)
        train_y.append([y])
    print('hit')
model.fit(train_x,
          train_y,
          nb_epoch=100,
          shuffle=True
          )
model.save_weights('model/' + str(int(time.time())) + '.result')
