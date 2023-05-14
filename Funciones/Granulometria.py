import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from .valoresentrada import *


FrameGranulometria=pd.DataFrame({ #creacion dataframe llamado "Granulometria" con primer columna "malla"
"Malla":malla
})
FrameGranulometria["Abertura(mm)"]=abertura #Llamando la serie abertura en el dataframe
FrameGranulometria["Retenido (g)"]=retenido #Llamando la serie retenido en el dataframe
Peso=FrameGranulometria['Retenido (g)'].sum() #Peso total de la granulometria
FrameGranulometria["Retenido Acum (g)"]=FrameGranulometria['Retenido (g)'].cumsum()
FrameGranulometria["Retenido Acum (%)"]=((FrameGranulometria['Retenido (g)'].cumsum())/Peso)*100 #Agregando el acum mediante la opcion cumsum
FrameGranulometria["Pasa (g)"]=Peso-FrameGranulometria['Retenido Acum (g)'] #Material pasante en gramos
FrameGranulometria["Pasa (%)"]=FrameGranulometria['Pasa (g)']*100/Peso #Material pasante en gramos en porcentaje
pasa=FrameGranulometria["Pasa (%)"] #nombro Pasa para usarla mas delante 
pd.options.display.float_format = '{:.3f}'.format #Para que el dataframe quede con 3 decimales

def Grafica():
    #Se grafica la línea de la granulometría
    plt.figure(figsize=(14, 5)) 
    plt.plot(abertura,FrameGranulometria["Pasa (%)"],linestyle='-', marker='o', color='k', fillstyle='none',label='Data') 
    f = interp1d(FrameGranulometria["Pasa (%)"], abertura)
    #grafica
    plt.xlabel('Diámetro (mm)')
    plt.ylabel('Porcentaje pasa (%)')
    plt.legend() 
    plt.xscale("log")
    plt.xlim(0.075,4.75)
    plt.ylim(0,100) 
    plt.grid(color='k',lw='0.1',ls='-')
    #se agregan más grillas
    ax1 = plt.gca()
    ax1.invert_xaxis()
    # Agregar el segundo eje x para los nombres de los tamices
    ax2 = ax1.twiny()
    ax2.set_xscale('log')
    ax2.set_xticks(abertura)
    ax2.set_xticklabels(malla, rotation=90, fontsize=8)
    # Agregar lineas de los tamices
    ax2.set_xlabel('Tamices')
    ax2.set_xlim(0.075,4.75)
    ax2.invert_xaxis()
    #agregamos nombre lineas verticales
    L_No10=([4.75,4.75])
    L_No20=([2,2])
    L_No40=([0.85,0.85])
    L_No60=([0.425,0.425])
    L_No140 = ([0.106,0.106]) 
    L_rango = ([0,100])
    #se indicca en el plot la ubicación de estas líneas
    plt.plot(L_No10, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No20, L_rango, color='grey', lw='0.8', ls='--') 
    plt.plot(L_No40, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No60, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No140, L_rango, color='grey', lw='0.8', ls='--')
    #se agrega textos
    plt.text(4.65,10,'Grava(fina)',fontsize=8,rotation=90)
    plt.text(1.95, 2, 'Arena(Gruesa)', fontsize=8, rotation=90)
    plt.text(0.415, 2, 'Arena(Mediana)', fontsize=8, rotation=90)
    plt.text(0.072, 2, 'Arena(Fina)', fontsize=8, rotation=90)

    x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
    for x in x_values:
        plt.axvline(x=x, color='grey', ls='-', lw='0.3')
    plt.show()
