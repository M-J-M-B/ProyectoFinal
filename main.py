# ENUNCIADO MINI-PROYECTO FINAL
# ENTREGA: DICIEMBRE 6 DE 2023
# Talento TICs 2023
# Python Avanzado (Python con librerías de análisis de datos)

# PYTHON Y ANÁLISIS DE DATOS: 
# (A) MODULO/SCRIPT EN PYTHON PARA CARGA/PROCESAMIENTO/ANALISIS Y VISUALIZACIÓN DE
#     COMPORTAMIENTO DE DATASETS
# (B) PRESENTACIÓN FINAL

# MENU DE OPCIONES:
# 1. CARGAR DATASET - SELECCIONAR UNO DE DOS DATASETS ELEGIDOS POR CADA UNO, 
#                     UNO DE LOS CUALES DEBE CONTENER AL MENOS UNA SERIE DE TIEMPO                     
# 2. REALIZAR LIMPIEZA DEL DATASET (realizar la limpieza del dataset,)
#                           mostrar mensaje de retroalimentación al usuario 
#                     2.1 GUARDAR DATASET LIMPIO
# 3. REALIZAR TAREAS DE ANÁLISIS BÁSICAS DEL DATASET:
#                     3.1 MOSTRAR PARÁMETROS ESTADÍSTICOS DEL DATASET
#                     3.2 MOSTRAR MATRIZ DE CORRELACIÓN
#                     3.3 REALIZAR OPERACIONES DE AGRUPAMIENTO Y AGREGACIÓN
#                     3.4 PARA EL DATASET CON SERIE DE TIEMPO, GENERAR DEBIDAMENTE
#                         LA TABLA PIVOTE
# 4. MOSTRAR AL MENOS 4 TIPOS DE GRÁFICOS, QUE EL USUARIO ELIJA (OFRECERLE OPCIONES)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import datetime
print(f"Se cargarán los siguientes datasets: MSFT(2000-2023) y EV_cars")
df_Stock = pd.read_csv("MSFT(2000-2023).csv")
df_Cars = pd.read_csv("EV_cars.csv")

#Se convierte la primera columna del dataser MSFT a fecha para su posterior análisis
df_Stock["Date"] = pd.to_datetime(df_Stock["Date"])

#Se define la función para graficar las tablas de correlación
def correlacion(x):
    if x == 2:
        df_factor = df_Cars.apply(lambda x: pd.factorize(x)[0])
        df_corr = df_factor.corr()
        plt.figure(figsize=(10,10))
        sb.heatmap(df_corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5)
        plt.title("Correlación de vehículos eléctricos")
        plt.show()
    if x == 1:
        df_factor = df_Stock.apply(lambda x: pd.factorize(x)[0])
        df_corr = df_factor.corr()
        plt.figure(figsize=(10,10))
        sb.heatmap(df_corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5)
        plt.title("Correlación de Stock en bolsa Microsoft")
        plt.show()

def visual1(x):
    if x == 1:
        pivot_table = pd.pivot_table(
            df_Stock,
            values=["Close", "Volume"],
            index=["Date"],
            aggfunc={"Close": ["sum"], "Volume": ["sum"]},
        )
        print(pivot_table)
    if x == 2:
        plt.figure(figsize=(12, 6))
        plt.plot(df_Stock['Date'], df_Stock['Close'], label='Precio al cierre', color='blue')
        plt.title('Precio al cierre en función del tiempo')
        plt.xlabel('Fecha')
        plt.ylabel('Precio al cierre')
        plt.legend()
        plt.grid(True)
        plt.show()
    if x == 3:
        fig, ax = plt.subplots(figsize=(20, 8))
        ax.plot(df_Stock['Date'], df_Stock['Volume'])
        ax.xaxis.set_major_locator(plt.MaxNLocator(15))
        ax.set_xlabel('Fecha', fontsize=14)
        ax.set_ylabel('Volumen', fontsize=14)
        plt.title('Tendencia del volumen de Microsoft', fontsize=18)
        plt.grid()
        plt.show()
    if x == 4:
        df_Stock['Market Cap'] = df_Stock['Open'] * df_Stock['Volume']
        fig, ax = plt.subplots(figsize=(20, 8))
        ax.bar(df_Stock['Date'], df_Stock['Market Cap'], color='black')
        ax.xaxis.set_major_locator(plt.MaxNLocator(15))
        ax.set_xlabel('Fecha', fontsize=14)
        ax.set_ylabel('Capitalización', fontsize=14)
        plt.title('Capitalización del mercado', fontsize=18)
        plt.grid()
        plt.show()
def visual2(x):
    if x == 1:
        sb.lmplot(
            data=df_Cars,
            x='acceleration..0.100.',
            y='Price.DE.'
        )
        plt.xlabel("Aceleración(0-100 Km/h)")
        plt.ylabel("Precio(USD)")
        plt.title("Precio en función de la aceleración")
        plt.show()
    if x == 2:
        plt.figure(figsize=(12,8))
        sb.scatterplot(data=df_Cars, x='Battery', y=('Top_speed'), hue='Price.DE.')
        plt.title('Vel. máxima en función de la batería con disperción por precio')
        plt.xlabel('Batería (kWh)')
        plt.ylabel('Velocidad máxima (Km/h)')
        plt.show()
    if x == 3:
        sb.histplot(data=df_Cars, y='Price.DE.', color='g')
        plt.title('Conteo de vehículos por precio')
        plt.xlabel('Conteo (unidades)')
        plt.ylabel('Precio (USD)')
        plt.tight_layout()
        plt.show()
    if x == 4:
        df_deportivos = df_Cars[(df_Cars['Top_speed'] >= 240) & (df_Cars['Efficiency'] <= 190)]

        plt.figure(figsize=(7,5))
        df_deportivos_bateria = df_deportivos.sort_values('Battery')
        sb.barplot(data=df_deportivos_bateria, y='Car_name', x='Price.DE.', hue='Battery')

        plt.xticks(rotation=90)
        plt.legend(title='Batería', bbox_to_anchor=(1.45,0.5))
        plt.title('Deportivos por batería y precio')
        plt.show()

datos, graph = int(input("Cual dataset quieres analizar ?\n1. MSFT\n2. EV_cars\nTu respuesta: ")), 0
if datos != 1 or 2:
    print("Solo se admiten los enteros 1 o 2 sin espacios, reinicie el programa")

if datos == 1:
    print("Se analizará el dataset MSFT(2000-2023) con las siguientes características:\n")
    df_Cars.info()
    print("\nVerificación de datos duplicados:\n")
    print(df_Cars.duplicated())
    print("\nEl dataset no contiene datos nulos ni duplicados.\n")
    print(f"A continuación algunas estadísticas del dataset:\n\n{df_Stock.describe()}")
    vizcorr= int(input("Escribir 1 para visualizar tabla de correlación: \n"))
    if vizcorr == 1:
        print(correlacion(1))
    if vizcorr != 1:
        print("\nSolo se admite el entero 1 sin espacios para continuar\n")
        vizcorr= int(input("Escribir 1 para visualizar tabla de correlación: \n"))
        if vizcorr == 1:
            print(correlacion(1))
    graph = int(input("Elija a continuación un gráfico para visualizar:\n1. Tabla pivote básica(Tabla)\n2. Precio al cierre (gráfico de línea)\n3. Tendencia del volumen de Microsoft (gráfico de línea de computación reducida)\n4. Capitalización del Mercado (gráfico de barras)\nTu respuesta: \n"))
    if graph == 1 or 2 or 3 or 4:
        visual1(graph)
    if graph != 1 or 2 or 3 or 4:
        print("Solo se admiten los enteros 1;2;3 y 4\n")
        graph = int(input("Elija a continuación un gráfico para visualizar:\n1. Tabla pivote básica(Tabla)\n2. Precio al cierre (gráfico de línea)\n3. Tendencia del volumen de Microsoft (gráfico de línea de computación reducida)\n4. Capitalización del Mercado (gráfico de barras)\nTu respuesta: \n"))
        if graph == 1 or 2 or 3 or 4:
            visual1(graph)
if datos == 2:
    print("\nSe analizará el dataset EV_cars con las siguientes características:\n")
    df_Cars.info()
    print("\nVerificación de datos duplicados:\n")
    print(df_Stock.duplicated())
    print("\nEl dataset contiene datos nulos pero no duplicados.\n\nComenzando limpieza...\n")
    df_Cars["Price.DE."] = df_Cars["Price.DE."].fillna(df_Cars['Price.DE.'].mean())
    df_Cars["Fast_charge"] = df_Cars["Fast_charge"].fillna(df_Cars['Fast_charge'].mean())
    print("Limpieza terminada, los datos nulos fueron reemplazados con el promedio de los datos de la columna:\n")
    df_Cars.info()
    print(f"\nA continuación algunas estadísticas del dataset:\n\n{df_Cars.describe()}")
    vizcorr= int(input("Escribir 1 para visualizar tabla de correlación: \n"))
    if vizcorr == 1:
        print(correlacion(2))
    if vizcorr != 1:
        print("\nSolo se admite el entero 1 sin espacios para continuar\n")
        vizcorr= int(input("Escribir 1 para visualizar tabla de correlación: \n"))
        if vizcorr == 1:
            print(correlacion(2))
    graph = int(input("A continuación elija un gráfico para visualizar:\n1. Aceleración en función del precio (gráfico preciso con tendencia)\n2. Vel. máxima en función de la batería con disperción por precio (gráfico de disperción)\n3. Conteo de vehículos por precio (gráfico de barras horizontal)\n4. Deportivos por batería y precio (gráfico de barras horizontal agrupado)\nTu respuesta: "))
    if graph == 1 or 2 or 3 or 4:
        visual2(graph)
    if graph != 1 or 2 or 3 or 4:
        print("Solo se admiten los enteros 1;2;3 y 4\n")
        graph = int(input("A continuación elija un gráfico para visualizar:\n1. Aceleración en función del precio (gráfico preciso con tendencia)\n2. Vel. máxima en función de la batería con disperción por precio (gráfico de disperción)\n3. Conteo de vehículos por precio (gráfico de barras horizontal)\n4. Deportivos por batería y precio (gráfico de barras horizontal agrupado)\nTu respuesta: "))
        if graph == 1 or 2 or 3 or 4:
            visual2(graph)