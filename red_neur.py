import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense

df = pd.read_csv("partidos_historicos.csv")

# Codificar variables categóricas
encoder = LabelEncoder()
df["Equipo_Local"] = encoder.fit_transform(df["Equipo_Local"])
df["Equipo_Visitante"] = encoder.fit_transform(df["Equipo_Visitante"])
df["Resultado"] = encoder.fit_transform(df["Resultado"])

# Dividir los datos en conjuntos de entrenamiento y prueba
X = df[["Equipo_Local", "Equipo_Visitante", "Cuota_Local", "Cuota_Visitante"]]
y = df["Resultado"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_shape=(4,), activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=32)

test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)

model.save('red_neur.h5')