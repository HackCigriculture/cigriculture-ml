from keras.models import Sequential
from keras.layers import Dense, Dropout, GaussianNoise


def network():
    return Sequential([
        Dense(8, input_shape=(2,), activation='relu'),
        GaussianNoise(0.05),
        Dense(16, activation='relu'),
        Dense(32, activation='relu'),
        Dropout(0.3),
        Dense(16, activation='relu'),
        Dense(4, activation='relu'),
        Dense(1, activation='relu')
    ])
