import pandas as pd

# Ruta al archivo .csv (ajusta la ruta según tu archivo)
archivo_csv = 'C:\Users\fvillagra\Downloads\TRABAJO EN CURSO DESARROLLO\health_data.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)

# Mostrar las primeras filas del archivo
print(df.head())
