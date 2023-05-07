from Funciones.CartaPlasticidad import *
from Funciones.Granulometria import *
from Funciones.clasificacion import *
import pandas as pd

if Pasa_Tamiz200>50: #Granos finos
    print("El material corresponde a Granos Finos")
    ResultadosCarta()
       
else: #Granos Gruesos
    print("El material corresponde a Granos gruesos")
    if Pasa_Tamiz4>50:
        if Pasa_Tamiz200<5:#Analizar Cu y CC
            if CU>6 and 1<CC<3:
                print("Arena bien graduada")
            else:
                print("Arena pobremente graduada")
        elif 5<Pasa_Tamiz200<12:#Analizar Cu, CC y carta de plasticidad
            if CU>6 and 1<CC<3:
                print("Arena bien graduada")
                ResultadosCarta()
                print("Es una arena bien graduada con",ResultadosCarta())
                ResultadosCarta()
            else:
                print("Arena pobremente graduada")
                ResultadosCarta()
                print("Es una Arena pobremente graduada con",ResultadosCarta())
                ResultadosCarta()
        else: #Analizar carta de plasticidad
            print("Arena")
            if CU>6 and 1<CC<3:
                print("Es una Arena limosa")
                ResultadosCarta()
            else:
                print("Es una Arena arcillosa")
                ResultadosCarta()
    else: #Gravas
        if Pasa_Tamiz200<5:#Analizar Cu y CC
            if CU>4 and 1<CC<3:
                print("Grava bien graduada")
            else:
                print("Grava pobremente graduada")
        elif 5<Pasa_Tamiz200<12:#Analizar Cu, CC y carta de plasticidad
            if CU>6 and 1<CC<3:
                print("Grava bien graduada")
                ResultadosCarta()
                print("Es una Grava bien graduada con",ResultadosCarta())
                ResultadosCarta()
            else:
                print("Grava pobremente graduada")
                print(ResultadosCarta())
                print("Es una Grava pobremente graduada con",ResultadosCarta())
                ResultadosCarta()
        else: #Analizar carta de plasticidad
            print("Grava") 
            if ResultadosCarta()=="Limos de baja plasticidad":
                print("Es una Grava limosa")
                ResultadosCarta()
            else:
                print("Es una Grava arcillosa")
                ResultadosCarta()
