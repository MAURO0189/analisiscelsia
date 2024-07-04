from generators.generateProduct import generateProduct
import pandas as pd

def analizarDatos():
    datos=generateProduct()
    tabla=pd.DataFrame(datos,columns=["product","category"])
    tabla.to_csv("./data/products.csv",index=False)
analizarDatos()