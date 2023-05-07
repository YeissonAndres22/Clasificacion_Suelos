from Funciones.CartaPlasticidad import *
from Funciones.Granulometria import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

#Porcentajes Pasa para hacer la INTERPOLACION
Pasa_Tamiz4=Granulometria.loc[Granulometria['Malla'] == '#4', 'Pasa (%)'].iloc[0] #Porcentaje pasa tamiz 4
Pasa_Tamiz10=Granulometria.loc[Granulometria['Malla'] == '#10', 'Pasa (%)'].iloc[0] #Porcentaje pasa tamiz 10
Pasa_Tamiz20=Granulometria.loc[Granulometria['Malla'] == '#20', 'Pasa (%)'].iloc[0] #Porcentaje pasa tamiz 20
Pasa_Tamiz40=Granulometria.loc[Granulometria['Malla'] == '#40', 'Pasa (%)'].iloc[0] #Porcentaje pasa tamiz 40
Pasa_Tamiz60=Granulometria.loc[Granulometria['Malla'] == '#60', 'Pasa (%)'].iloc[0] #Porcentaje pasa tamiz 60
Pasa_Tamiz140=Granulometria.loc[Granulometria['Malla'] == '#140', 'Pasa (%)'].iloc[0] #Porcentaje pasa tamiz 140
Pasa_Tamiz200=Granulometria.loc[Granulometria['Malla'] == '#200', 'Pasa (%)'].iloc[0] #Porcentaje pasa tamiz 200

#INTERPOLACION D10
# Seleccionar la primera fila que tenga un valor inferior a 10 en la columna "Pasa (%)"
fila_inf_D10= Granulometria.loc[Granulometria['Pasa (%)'] < 10].iloc[0]
# Seleccionar la fila anterior
fila_sup_D10 = Granulometria.iloc[fila_inf_D10.name - 1]
# Extraer los valores de la columna "Pasa (%)"
valor_inf_D10 = fila_inf_D10['Pasa (%)']
valor_sup_D10 = fila_sup_D10['Pasa (%)']
# Extraer los valores de la columna "Abertura (mm)"
abertura_inf_D10 = fila_inf_D10['Abertura (mm)']
abertura_sup_D10 = fila_sup_D10['Abertura (mm)']
#Se aplica la formula para hallar los Ds
D10=(((abertura_inf_D10-abertura_sup_D10)/(valor_inf_D10-valor_sup_D10))*(10-valor_sup_D10))+abertura_sup_D10

#INTERPOLACION D30
# Seleccionar la primera fila que tenga un valor inferior a 30 en la columna "Pasa (%)"
fila_inf_D30= Granulometria.loc[Granulometria['Pasa (%)'] < 30].iloc[0]
# Seleccionar la fila anterior
fila_sup_D30 = Granulometria.iloc[fila_inf_D30.name - 1]
# Extraer los valores de la columna "Pasa (%)"
valor_inf_D30 = fila_inf_D30['Pasa (%)']
valor_sup_D30 = fila_sup_D30['Pasa (%)']
# Extraer los valores de la columna "Abertura (mm)"
abertura_inf_D30 = fila_inf_D30['Abertura (mm)']
abertura_sup_D30 = fila_sup_D30['Abertura (mm)']
#Se aplica la formula para hallar los Ds
D30=(((abertura_inf_D30-abertura_sup_D30)/(valor_inf_D30-valor_sup_D30))*(30-valor_sup_D30))+abertura_sup_D30

#INTERPOLACION D60
# Seleccionar la primera fila que tenga un valor inferior a 60 en la columna "Pasa (%)"
fila_inf_D60= Granulometria.loc[Granulometria['Pasa (%)'] < 60].iloc[0]
# Seleccionar la fila anterior
fila_sup_D60 = Granulometria.iloc[fila_inf_D60.name - 1]
# Extraer los valores de la columna "Pasa (%)"
valor_inf_D60 = fila_inf_D60['Pasa (%)']
valor_sup_D60 = fila_sup_D60['Pasa (%)']
# Extraer los valores de la columna "Abertura (mm)"
abertura_inf_D60 = fila_inf_D60['Abertura (mm)']
abertura_sup_D60 = fila_sup_D60['Abertura (mm)']
#Se aplica la formula para hallar los Ds
D60=(((abertura_inf_D60-abertura_sup_D60)/(valor_inf_D60-valor_sup_D60))*(60-valor_sup_D60))+abertura_sup_D60

#Calcular el valor de CC y CU
CC=(D30**(2))/(D60*D10)
CU=D60/D10

def ResultadosCarta():
    LL=int(input("Ingrese limite liquido "))
    IP=int(input("Ingrese indice de plasticidad "))
    yLineaU = 0.9*(LL-8)
    yLineaA = 0.73*(LL-20)
    
    if LL>50: #Alta Plasticidad
        if 0<IP<yLineaA:#MH
            print("Limos de alta plasticidad")
        elif yLineaA<IP<yLineaU: #CH
            print("Arcillas de alta plasticidad")
        else:
            print("NO EXISTE") #NO EXISTE
    else: #Baja plasticidad
        if 0<yLineaA: #ML
            print("Limos de baja plasticidad")
        elif yLineaA<yLineaU and 0<IP<4:#ML
            print("Limos de baja plasticidad")
        elif yLineaA<yLineaU and 4<IP<7:#CL-ML
            print("Arcillas de baja plasticidad-ML=Limos de baja plasticidad")
        elif yLineaA<yLineaU and 7<IP:#CL
            print("Arcillas de baja plasticidad")
        else:
            print("NO EXISTE")
    
    CartaDePlasticidad(LL,IP)
