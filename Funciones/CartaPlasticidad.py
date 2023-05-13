import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear la gráfica con ambas líneas
def CartaDePlasticidad(LL, IP):
    x = np.linspace(0, 100, 100)                                                      #Asigno valores de x desde 0 a 100, hagalo 100 veces
    yLineaU = 0.9*(x-8)                                                               #Funcion de Y con respecto a X para la linea U de la grafica
    yLineaA = 0.73*(x-20)                                                             #Funcion de Y con respecto a X para la linea A de la grafica
    y1=7                                                                              #linea con y=7 
    y2=4                                                                              #linea con y=4 
    plt.figure(figsize=(20,12))                                                       #Tamaño de la grafica en X y Y
    LineaU=plt.plot(x, yLineaU, label='Linea U',color='red')                          #Imprima una linea teniendo en cuenta X,yLineaU, nombrela como Linea U y dele color rojo
    LineaA=plt.plot(x, yLineaA, label='Linea A',color='black')                        #Imprima una linea teniendo en cuenta X,yLineaA, nombrela como Linea A y dele color negro
    plt.axvline(x=50, color='black', linestyle='--',lw=1.2)                           #Dibuje una linea en x=50 que sea de color negro con estilo discontinuo '--' y transparencia 1.2
    plt.axvline(x=80, color='black', linestyle='--',lw=1.2)                           #Dibuje una linea en x=80 que sea de color negro con estilo discontinuo '--' y transparencia 1.2
    plt.hlines(y=7, xmin=7/0.9+8, xmax=7/0.73+20, linestyle='--', color='black', lw=0.7)                                #Crea una linea con Y=7 en un rango intervalo de x
    plt.hlines(y=4, xmin=4/0.9+8, xmax=4/0.73+20, linestyle='--', color='black', lw=0.7)                                #Crea una linea con Y=4 en un rango intervalo de x
    Cuadrilatero0=plt.fill([20,8 , y2/0.9+8, y2/0.73+20], [0,0, y2, y2], 'y', alpha=0.5)                             #Le asigna un color a una zona determinada ingresando las coordenadas de X y Y
    Cuadrilatero1= plt.fill([y2/0.73+20,y2/0.9+8 , y1/0.9+8, y1/0.73+20], [y2, y2, y1, y1], 'black', alpha=0.5)         #Le asigna un color a una zona determinada ingresando las coordenadas de X y Y
    Cuadrilatero2= plt.fill([50,50, y1/0.9+8, y1/0.73+20], [0.73*(50-20), 0.9*(50-8), y1, y1], 'g', alpha=0.5)          #Le asigna un color a una zona determinada ingresando las coordenadas de X y Y
    Cuadrilatero3= plt.fill([50,50, 60/0.9+8, 60/0.73+20], [0.73*(50-20), 0.9*(50-8), 60, 60], 'grey', alpha=0.5)       #Le asigna un color a una zona determinada ingresando las coordenadas de X y Y
    Cuadrilatero4= plt.fill([50,50,60/0.73+20,60/0.73+20], [0,0.73*(50-20),60,0], 'm', alpha=0.5)                       #Le asigna un color a una zona determinada ingresando las coordenadas de X y Y
    Triangulo= plt.fill([20,50,50], [0,0,0.73*(50-20)], 'y', alpha=0.5)                                                 #Le asigna un color a una zona determinada ingresando las coordenadas de X y Y
    plt.grid(color='g',lw=1.4,ls=':')       #Coloca grilla al grafico
                                                               
# Agregar leyendas y títulos
    plt.xlabel('LIMITE LIQUIDO',fontsize=18)                       #Nombre al eje x como limite liquido
    plt.ylabel('INDICE DE PLASTICIDAD',fontsize=18)                #Nombre al eje y como limite plasticidad
    plt.title('CARTA DE PLASTICIDAD',fontsize=28)                  #Nombre de la grafica
    plt.ylim(0, 60)                                                #Rango de la grafica en X
    plt.xlim(0, 100)                                               #Rango de la grafica en Y

    plt.legend()
#Creacion del punto LL y IP
    Limite_liquido = LL
    Indice_plasticidad = IP

    plt.plot(Limite_liquido,Indice_plasticidad,'bo')
    plt.vlines(Limite_liquido,0,60,'k','--',color='m')
    plt.annotate(' LL ', (Limite_liquido+0.5,51))
    plt.annotate(' IP ', (45,Indice_plasticidad+1))
    plt.hlines(Indice_plasticidad,0,100,'k','--',color='g')
#Etiquetas de las lineas
    plt.annotate('Linea A', (70,35),rotation=35,fontsize=15) # Etiqueta de la linea A
    plt.annotate('Linea U', (65,50),rotation=42,fontsize=15) # Etiqueta de la linea U
# Graficamos lineas frontera de la carta de plasticidad donde se encuentran los suelos CL-ML
    plt.annotate('CL-ML',(18,5),fontsize=15)
    plt.annotate('MH', (75,22),fontsize=15)
    plt.annotate('CL', (34,17),fontsize=15)
    plt.annotate('CH', (64,42),fontsize=15)
    plt.annotate('ML', (37,6),fontsize=15)
    plt.annotate('NO EXISTE', (17,35),fontsize=15)
# Mostrar la gráfica
    plt.show()
