import numpy as np
import pandas as pd

#Ejercicio 1
a = np.random.randint(low=0, high=10, size=(5, 3))
df = pd.DataFrame(data=a, columns=['A', 'B', 'C'])

def funcion1(dataframe, col):
    dataframe[col]=np.mean(dataframe[col])
    return dataframe

def funcion2(dataframe):
    return dataframe.abs()

def funcion3(dataframe, col, col1):
    dataframe[col1]=(dataframe[col]+dataframe[col1])
    return dataframe

print(df.pipe(funcion1, 'A').pipe(funcion2).pipe(funcion3, 'B', 'C'))

#Ejercicio 4
meses = np.random.randint(low=5000, high=10000, size=(12, 3))
df1 = pd.DataFrame(data=meses, columns=['Carne', 'Huevos', 'Queso'])
#df1.set_index([pd.Index(['Enero','Febrero','Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
#               'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])])
    
def dolares(dataframe):
    return dataframe*0.00029

def pesos(dataframe):
    return dataframe.abs()

def euros(dataframe):
    return dataframe*0.00027

def libras(dataframe):
    return dataframe*0.00024

print(df1.transform([pesos, dolares, euros, libras]).set_index([pd.Index(['Enero',
      'Febrero','Marzo', 'Abril', 'Mayo', 'Junio', 'Julio','Agosto', 'Septiembre', 
      'Octubre', 'Noviembre', 'Diciembre'])]))

#Ejercicio 5
print(df1.applymap(dolares).set_index([pd.Index(['Enero','Febrero','Marzo', 
      'Abril', 'Mayo', 'Junio', 'Julio','Agosto', 'Septiembre', 'Octubre', 
      'Noviembre', 'Diciembre'])]))
