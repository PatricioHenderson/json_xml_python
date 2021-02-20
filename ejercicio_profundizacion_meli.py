#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''



import json
import requests
import matplotlib.pyplot as plt



def fetch():
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

    response = requests.get(url)
    dataset = response.json()
    json_response = dataset["results"]
    
    filtrado = [{"price": x["price"], "condition": x["condition"]} for x in json_response if x["currency_id"] == "ARS"]
    """
    with open ("meli","w") as json_file:
        json.dump(filtrado, json_file, indent=4)
    """
    return  filtrado
def transform(dataset,min,max):
    lista1 = []
    lista2 = []
    lista3 = []
    
    for i in dataset:
        if i["price"] <= min:
            lista1.append(i)
        if  min < i["price"]  < max:
            lista2.append(i)
        if i["price"] >= max:
            lista3.append(i)

    min_count = len(lista1)
    min_max_count = len(lista2)
    max_count = len(lista3)
    print(min_count, min_max_count, max_count)
    return [min_count, min_max_count, max_count]
    
def report(data):
    fig = plt.figure()
    fig.suptitle("Alquileres en Mendoza")

    ax = fig.add_subplot()
    ax.pie(data,labels=(min,"Entre {} y {}".format(min,max1),max), autopct="%1.1f%%")
    plt.show()



if __name__ == "__main__":
    
    min = int(input("Ingresar valor minimo "))
    max = int(input("Ingresar valor máximo "))

    dataset = fetch()
    data = transform(dataset,min,max)
    report(data)
    