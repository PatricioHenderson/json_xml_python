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

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import matplotlib.pyplot as plt

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede inventar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_data = {
        "nombre": "Patricio",
        "apellido":"Henderson",
        "dni":"93.852.079",
        "vestimenta":
          [
          { "prenda": "zapatilla", "cantidad": 4 },
          { "prenda": "remeras", "cantidad": 12 }
          ]
               }

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina
    json_string = json.dumps(json_data)
    print("Ejercicio 1, Json a string", json_string)
    # Observe el archivo y verifique que se almaceno lo deseado
    
    with open ("json_data", "w") as jsonfile:

        json.dump(json_data,jsonfile, indent=4)    
    pass
    

def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    with open ("json_data","r") as jsonfile:

        json_data = json.load(jsonfile)
        print("Deserialize json" , json_data)
        

        json_string = json.dumps(json_data)
        print("Json a string" , json_string)
        
        pass
    
    

def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.
    pass


def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.
    pass


def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    

    #info = response.json()
    info = json.loads(response.text)
    
    contadoruser1 = 0
    for user in info:
        if user ["userId"] == 1 and user ["completed"] == True:
            contadoruser1 +=1
    
    contadoruser2 = 0
    for user in info:
        if user ["userId"] == 2 and user ["completed"] == True:
            contadoruser2 +=1

    contadoruser3 = 0
    for user in info:
        if user ["userId"] == 3 and user ["completed"] == True:
            contadoruser3 +=1        
    
    contadoruser4 = 0
    for user in info:
        if user ["userId"] == 4 and user ["completed"] == True:
            contadoruser4 +=1
    
    contadoruser5 = 0
    for user in info:
        if user ["userId"] == 5 and user ["completed"] == True:
            contadoruser5 +=1
    
    contadoruser6 = 0
    for user in info:
        if user ["userId"] == 6 and user ["completed"] == True:
            contadoruser6 +=1
    
    contadoruser7 = 0
    for user in info:
        if user ["userId"] == 7 and user ["completed"] == True:
            contadoruser7 +=1
    
    contadoruser8 = 0
    for user in info:
        if user ["userId"] == 8 and user ["completed"] == True:
            contadoruser8 +=1
    
    contadoruser9 = 0
    for user in info:
        if user ["userId"] == 9 and user ["completed"] == True:
            contadoruser9 +=1
        
    contadoruser10 = 0
    for user in info:
        if user ["userId"] == 10 and user ["completed"] == True:
            contadoruser10 +=1
    
    print((contadoruser1,contadoruser2,contadoruser3,contadoruser4,contadoruser5,contadoruser6,
            contadoruser7,contadoruser8,contadoruser9,contadoruser10))

    aprobados = ((contadoruser1,contadoruser2,contadoruser3,contadoruser4,contadoruser5,contadoruser6,
            contadoruser7,contadoruser8,contadoruser9,contadoruser10))

    users = (1,2,3,4,5,6,7,8,9,10)       
    fig = plt.figure()
    fig.suptitle("No me gusta como lo resolví!")

    ax = fig.add_subplot()
    
    ax.pie(aprobados , labels=users , autopct="%1.1f%%")
    plt.show()



    "Lo arme de nuevo en base a las correciones que ví en el foro y me gusta un poco más, costo pero lo entendí"




    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    
    data = json.loads(response.text)
    data = response.json()

    
    # Utilizando mascara

    filter_data = [x["userId"] for x in data if x.get("completed") is True] 
    
    
    print (filter_data)
    
    data = {}

    for i in filter_data:
        if (i in data) == False:
            data[i] = 0
        data[i] += 1
    users = []
    cursos= []
    for i in data:
        print("El usuario {} realizo {}  cursos".format(i,data[i]))
        
        users.append(i)
        cursos.append(data[i])
    
    
    fig = plt.figure()
    fig.suptitle ("ejercicio 5")

    ax = fig.add_subplot()

    ax.pie(cursos, labels=users , autopct="%1.1f%%")
    plt.show()





   
    
    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    # ej3()
    # ej4()
    ej5()
