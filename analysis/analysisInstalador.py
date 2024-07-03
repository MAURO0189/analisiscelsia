from generators.generadorInstalador import generateDataInstall
import pandas as pd

def analizarDatos():
    datos=generateDataInstall()
    tabla=pd.DataFrame(datos,columns=["responsable","edad","zona","experiencia","instalaciones"])
    tabla.to_csv("./data/instaladoresAburraSur.csv",index=False)
analizarDatos()