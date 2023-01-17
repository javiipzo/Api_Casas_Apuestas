#Calcular la probabilidad de que gane cada equipo segun local/visitante

# importar las librerias necesarias
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
# cargar los datos en un dataframe de pandas
df = pd.read_csv("partidos_historicos.csv") #inexistente de momento
df= df.dropna()

encoder = LabelEncoder()
df["Equipo_Local"] = encoder.fit_transform(df["Equipo_Local"])
df["Equipo_Visitante"] = encoder.fit_transform(df["Equipo_Visitante"])
# seleccionar las características del modelo y la variable objetivo
X = df[["Equipo_Local", "Equipo_Visitante", "Cuota_Local", "Cuota_Visitante"]]
y = df["Resultado"] #(1 para victoria local, 2 para empate, 3 para victoria visitante)

# dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# instanciar el modelo de regresión logística
model = LogisticRegression()


# entrenar el modelo utilizando el conjunto de entrenamiento
model.fit(X_train, y_train)

# hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

print("La precisión del modelo es: ", accuracy)

# guardar el modelo
import joblib

joblib.dump(model, "modelo_entrenado.pkl")