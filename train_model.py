import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

label_encoder = LabelEncoder()

#get data
trainData = pd.read_csv('./train/train.tsv', sep='\t',header=None)
testData = pd.read_csv('./test-A/in.tsv', sep='\t',header=None)

y = trainData[trainData.columns[0]]
x = trainData.ix[1,]

droppedTrainData = trainData.drop(trainData.columns[[0]], axis=1)

for col in droppedTrainData:
   droppedTrainData[col] = label_encoder.fit_transform(droppedTrainData[col])

for col in testData:
    testData[col] = label_encoder.fit_transform(testData[col])

X = droppedTrainData
Y = trainData[trainData.columns[0]].apply(lambda x: 1 if x == "p" else 0)

#define the neural network
model = Sequential()
model.add(Dense(32, input_dim=22, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#compile the network
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the network
history = model.fit(X, Y, epochs=20, batch_size=10)

#evaluate the network
loss, accuracy = model.evaluate(X, Y)
print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))

# serialize model to JSON
model_json = model.to_json()
with open("model/model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model/model.h5")
print("Saved model to disk")
