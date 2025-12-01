import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
import joblib # to save the scaler for later use

# 1. load the data
# this is the clean data we just generated from the monday pcap
data_file = "training_data.csv"
print("[*] Loading training data...")
df = pd.read_csv(data_file)

# 2. preprocessing (normalization)
# neural networks hate big numbers. we squash everything between 0 and 1.
scaler = MinMaxScaler()
x_train = scaler.fit_transform(df.values)

# save the scaler! we need it later to normalize the 'attack' traffic exactly the same way
joblib.dump(scaler, "scaler.save")
print("[*] Data normalized and scaler saved.")

# 3. build the autoencoder model
# input dim is 8 because we have 8 columns in our csv
input_dim = x_train.shape[1]

model = Sequential()

# encoder: compressing the information
model.add(Dense(6, activation='relu', input_shape=(input_dim,)))
model.add(Dense(4, activation='relu'))

# decoder: decompressing it back
model.add(Dense(6, activation='relu'))
model.add(Dense(input_dim, activation='sigmoid')) # sigmoid outputs 0-1, matches our normalized data

# 4. compile the model
# 'mean_squared_error' is our loss function. we want input == output.
model.compile(optimizer='adam', loss='mean_squared_error')

# 5. train
print("[*] Starting training...")
# epochs=10 means it sees the data 10 times. batch_size=32 is standard.
history = model.fit(x_train, x_train, 
                    epochs=10, 
                    batch_size=32,
                    shuffle=True,
                    validation_split=0.1)

# 6. save the brain
model.save("nids_autoencoder.keras")
print("\n[SUCCESS] Model trained and saved as 'nids_autoencoder.keras'")