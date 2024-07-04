import random

def generateProduct():
    products = ["Musica","Tv","Aplicaciones","Pc","Celulares","Tablets","Accesorios"]
    data = []
    for product in products:
        store = {}
        category = random.choice(["plus","mega","basic"])
        store = [product,category]
        data.append(store)

    return data 

print(generateProduct())    
