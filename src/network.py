from keras.models import Sequential
from keras.layers import Dense


def network():
    return Sequential([
        Dense(8, input_shape=(2,), activation='relu'),
        Dense(16),
        Dense(32),
        Dense(16),
        Dense(4),
        Dense(1, activation='relu')
    ])
