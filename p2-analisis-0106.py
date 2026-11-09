# importar librerias
import pandas as pd
import numpy as np
# Samuel Nicola NC 0106
print("Analisis de datos Transacciones Samuel Nicola NC = 0106")
transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [16.50, 15.00, 12.00, 890.00, 12.00, 15.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}
df = pd.DataFrame(transacciones)
print(df)
print("-+-+-+ Agrupar por una sola columna Monto -+-+-+")
agrupados = df.groupby('Monto')
print(agrupados)
print("-+-+-+ monto de transaccione -+-+-+")
# Ubicacion inusual por transaccion
print(agrupados["Ubicacion_Inusual"].mean())
print("Fraude verdadero o falso")
# Fraude por transaccion
print(agrupados["Es_Fraude"].max())

print("-*-*-*Samuel Nicola segunda parte NC 0106 -*-*-*")
print("Agregacion multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupados['Ubicacion_Inusual'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupacion por varias columnas")
print("Agrega columna al dataframe")
print("Columna Team --> Equipo")
df['Equipo'] = ['A','B','A','B','A','B']
agrupacion_multiple = df.groupby(['Monto', 'Equipo'])['Ubicacion_Inusual'].mean()
print(agrupacion_multiple)