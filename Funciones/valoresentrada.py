import pandas as pd

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
80 #Fondo
])
