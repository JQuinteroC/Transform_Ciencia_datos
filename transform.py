import numpy as np
import pandas as pd

#Ejercicio 1
# Crear un ejemplo de pipe con tres funciones.
# La primera y la tercera función deben tener argumentos diferentes al dataframe
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

# EJERCICIO 2
# Mediante lambda cree una fución que permita obtener el IMC a partir de un data
# frame que contenga el peso y la estatura de personas.
estatura = np.random.randint(low = 120, high = 190, size = (15))
peso = np.random.randint(low = 15, high = 120, size = (15))
df2 = pd.DataFrame(data = estatura/100 , columns=['Estatura'])
df2['Peso'] = pd.DataFrame(data=peso)

print(df2.apply(lambda x: x[1] / x[0]**2, axis=1))


# EJERCICIO 3
# Mediante agg cree un dataframe resumen que contenga 5 valores estadísticos de
# un dataframe de entrada
estudiantes = {'Alumno':['Araceli','Manuel','Pablo','Íñigo','Mario','Raúl','Verónica',
                 'Darío','Laura','Silvia','Eduardo','Susana','María'],
    'Nota':[4,2.5,3,2,1.5,2,3,5,2,3,1,4,2.5]}
df3 = pd.DataFrame(data = estudiantes)

print(df3.agg(['mean', 'std', 'median', 'var']))

#Ejercicio 4
# Genere un dataframe donde se almacene el precio (en pesos colombianos) de 
    # algunos productos a través de los meses de un año
# A partir del dataframe anterior genere un nuevo dataframe donde los precios 
    # de los productos se encuentren en dolares, euros y libras.
meses = np.random.randint(low=5000, high=10000, size=(12, 3))
df1 = pd.DataFrame(data=meses, columns=['Carne', 'Huevos', 'Queso'])
    
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
# Realice el ejercicio 4 pero únicamento convirtiendo de pesos a dolares
print(df1.applymap(dolares).set_index([pd.Index(['Enero','Febrero','Marzo', 
      'Abril', 'Mayo', 'Junio', 'Julio','Agosto', 'Septiembre', 'Octubre', 
      'Noviembre', 'Diciembre'])]))
