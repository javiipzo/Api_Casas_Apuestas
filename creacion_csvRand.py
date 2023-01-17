import csv
import random

# Número de filas de datos aleatorios a generar
num_rows = 5000
list_equipos =['Ajax','Atlanta','Atletico','Barcelona','Bayern','Benfica','Bensiktas','Chelsea','Club Brugge','Dortmund','Dynamo','Internazionale','Juventus','Leipzig',
'Liverpool','LOSC','Malmö','Man. City','Man. United','Milan','Paris','Porto','Real Madrid','Salzburg','Sevilla','Shakhtar Donetsk','Sheriff','Sporting CP','Villareal',
'Wolfsburg','Young Boys','Zenit']

# Abrir un archivo CSV para escribir
with open('partidos_historicos.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Escribir la fila de encabezado en el archivo CSV
    csvwriter.writerow(['Equipo_Local', 'Equipo_Visitante', 'Cuota_Local', 'Cuota_Visitante', 'Resultado'])
    
    # Generar y escribir filas de datos aleatorios en el archivo CSV
    for i in range(num_rows):
        Num_e_local=random.randint(0,len(list_equipos)-1)
        Num_e_visitante=random.randint(0,len(list_equipos)-1)
        while Num_e_local==Num_e_visitante:
            Num_e_visitante=random.randint(0,len(list_equipos)-1)
        e_local=list_equipos[Num_e_local]
        e_visitante=list_equipos[Num_e_visitante]
        Cuotas_Local=random.randint(0,100)
        Cuotas_Visitante=100-Cuotas_Local
        Resultado=random.randint(1,3)

        row = [e_local,
               e_visitante,
               Cuotas_Local,
               Cuotas_Visitante,
               Resultado]
        csvwriter.writerow(row)