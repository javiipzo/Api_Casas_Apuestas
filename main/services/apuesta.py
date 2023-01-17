from main.map import ApuestaSchema
from main.repositories.repositorioapuesta import ApuestaRepositorio 
from main.repositories.repositoriocuota import CuotaRepositorio
from abc import ABC

apuesta_schema = ApuestaSchema()
apuesta_repositorio = ApuestaRepositorio()
cuota_repositorio = CuotaRepositorio()

class ApuestaService:

    def agregar_apuesta(self, apuesta, local, visitante):
        cuota = cuota_repositorio.find_by_partido(apuesta)
        probabilidad = self.set_cuota(cuota, local, visitante)
        apuesta.ganancia = round(apuesta.monto * probabilidad, 2)
        return apuesta_repositorio.create(apuesta)

    def set_cuota(self, cuota, local, visitante):
        if local:
            cuota_local = CuotaLocal()
            probabilidad = cuota_local.calcular_cuota(cuota)
            return probabilidad
        if visitante:
            cuota_visitante = CuotaVisitante()
            probabilidad = cuota_visitante.calcular_cuota(cuota)
            return probabilidad
        cuota_empate = CuotaEmpate()
        probabilidad = cuota_empate.calcular_cuota(cuota)
        return probabilidad

    def obtener_apuesta_por_id(self, id):
        return apuesta_repositorio.find_one(id)

    def obtener_apuestas_ganadas(self):
        return apuesta_repositorio.find_wins()

    def obtener_apuestas(self):
        return apuesta_repositorio.find_all()
#patron
class CuotaStrategy(ABC):
    def calcular_cuota(self, caracter_part): #donde las caracter son [0]=Equipo local [1]=Equipo visitante [2]=Cuota local [3]=Cuota visitante
        #from modelo_entr import model
        import joblib
        #o de la siguiente manera
        model= joblib.load("modelo_entrenado.pkl")
        """Calcular probabilidad"""
        probabilidad = model.predict_proba(caracter_part)

        '''
        O CON DEEP LEARNING

        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import LabelEncoder
        from tensorflow.python.keras import Sequential
        from tensorflow.python.keras.layers import Dense
        model=keras.models.load_model('red_neur.h5')
        predictions=model.predict(caracter_part)

        # Procesar la predicción
        probabilidad = predictions[0][1] if self.__class__.__name__ == "CuotaLocal" else predictions[0][2]

        '''
        return probabilidad
        

class CuotaLocal(CuotaStrategy):
    def calcular_cuota(self, cuota):
        probabilidad = cuota.cuota_local
        return probabilidad

class CuotaVisitante(CuotaStrategy):
    def calcular_cuota(self, cuota):
        probabilidad = cuota.cuota_visitante
        return probabilidad

class CuotaEmpate(CuotaStrategy):
    def calcular_cuota(self, cuota):
        probabilidad = cuota.cuota_empate
        return probabilidad