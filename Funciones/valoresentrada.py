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
58, #Tamiz 10
71, #Tamiz 20
83, #Tamiz 40
133, #Tamiz 60
246, #Tamiz 140
280, #Tamiz 200
480 #Fondo
])
