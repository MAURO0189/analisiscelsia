import random

def generateDataInstall():
    instaladores = ["Jhon doe","Pedro Perez","Ana Rubio","Carlos Zapata","Martha builes"]
    datos = []
    for instalador in instaladores:
        responsable = {}
        edad = random.randint(25,50)
        zona = random.choice(["zona A","zona B","zona C"])
        experiencia = random.randint(1,20)
        instalaciones = random.randint(20,50)
        responsable = [instalador,edad,zona,experiencia,instalaciones]
        datos.append(responsable)

    return datos

print(generateDataInstall())    
