import pandas as pd
def Granulometria():
    malla=pd.Series([
    "#4", #Tamiz 4
    "#10", #Tamiz 10
    "#20", #Tamiz 20
    "#40", #Tamiz 40
    "#60", #Tamiz 60
    "#140", #Tamiz 140
    "#200", #Tamiz 200
    "Fondo", #Pasa tamiz#200
    ])
    abertura=pd.Series([ #Malla en mm
    4.75, #Tamiz 4
    2,  #Tamiz 10
    0.85, #Tamiz 20
    0.425, #Tamiz 40
    0.25, #Tamiz 60
    0.106, #Tamiz 140
    0.075, #Tamiz 200
    0 #Fondo
    ])
    retenido=pd.Series([ #Material retenido por tamiz en gramos
    25,  #Tamiz 4
    38, #Tamiz 10
    71, #Tamiz 20
    43, #Tamiz 40
    33, #Tamiz 60
    26, #Tamiz 140
    480, #Tamiz 200
    180 #Fondo
    ])
    Granulometria=pd.DataFrame({ #creacion dataframe llamado "Granulometria" con primer columna "malla"
    "Malla":malla
    })
    Granulometria["Abertura (mm)"]=abertura #Llamando la serie abertura en el dataframe
    Granulometria["Retenido (g)"]=retenido #Llamando la serie retenido en el dataframe
    Peso=Granulometria['Retenido (g)'].sum() #Peso total de la granulometria
    Granulometria["Retenido Acum (g)"]=Granulometria['Retenido (g)'].cumsum()
    Granulometria["Retenido Acum (%)"]=((Granulometria['Retenido (g)'].cumsum())/Peso)*100 #Agregando el acum mediante la opcion cumsum
    Granulometria["Pasa (g)"]=Peso-Granulometria['Retenido Acum (g)'] #Material pasante en gramos
    Granulometria["Pasa (%)"]=Granulometria['Pasa (g)']*100/Peso #Material pasante en gramos en porcentaje
    pasa=Granulometria["Pasa (%)"] #nombro Pasa para usarla mas delante 
    pd.options.display.float_format = '{:.3f}'.format #Para que el dataframe quede con 3 decimales

