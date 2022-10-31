import json
import os
import random
os.system("cls")

with open("datacopy.json", encoding='utf-8') as archivo:
    info = json.load(archivo)

class Pregunta:
    def __init__(self, enunciado: str, alternativas: list, respuesta: str):
        self.__enunciado = enunciado
        self.__alternativas = alternativas
        self.__respuesta = respuesta
    
    def mostrarPregunta(self):
        #     print("\n" + str(indice+1) + ") " + datos["Valotario"][pregunta]["Pregunta"])
        print(self.__enunciado)
        random.shuffle(self.__alternativas)
        for alternativa in self.__alternativas:
            print("    " + alternativa)
        
# print(cuestionario[1]["Pregunta"])
# pregunta1 = Pregunta(info[0]["Pregunta"],info[0]["Alternativas"],info[0]["Respuesta"])
# pregunta1.mostrarPregunta()

listaPreguntas = []

for cuestionario in info:
    enunciado = cuestionario["Pregunta"]
    alternativas = cuestionario["Alternativas"]
    respuesta = cuestionario["Respuesta"]
    pregunta = Pregunta(enunciado,alternativas,respuesta)
    listaPreguntas.append(pregunta)

# Lista de preguntas del 1 al 10 en desorden
# ordenPreguntas = random.sample(range(len(datos["Valotario"])),10)
random.shuffle(listaPreguntas)

for pregunta in listaPreguntas:
    pregunta.mostrarPregunta()
    print("")









numero_intentos = []
puntaje_intentos = []
intentos = 1
numeroPreguntas = 10

letrasRespuestas = []  # Almacena las alternativas correctas
puntos_intento = []  # Almacena la puntuación en cada intento

# Lista de preguntas del 1 al 10 en desorden
# ordenPreguntas = random.sample(range(len(datos["Valotario"])),10)
# random.shuffle(ordenPreguntas)



# for indice, pregunta in enumerate(ordenPreguntas):
#     letrasDisponibles = []  # Almacena las alternativas disponibles
#     # Muestra la pregunta
#     print("\n" + str(indice+1) + ") " + datos["Valotario"][pregunta]["Pregunta"])

#     # Desordenar las alternativas
#     ordenAlternativas = [i for i in range(len(datos["Valotario"][pregunta]["Alternativas"]))]
#     random.shuffle(ordenAlternativas)

#     for letra, alternativa in enumerate(ordenAlternativas):  # Muestra las alternativas
#         print("    " + chr(letra+97) + ") " + datos["Valotario"][pregunta]["Alternativas"][alternativa])
#         # Guarda la siguiente letra de alternativa "a", "b", "c", "d", ...
#         letrasDisponibles.append(chr(letra+97))
#         # Comprueba la alternativa correcta
#         if datos["Valotario"][pregunta]["Alternativas"][alternativa] == datos["Valotario"][pregunta]["Respuesta"]:
#             # Almacena la alternativa correcta
#             letrasRespuestas.append(chr(letra+97))



























# nombre = input("Ingresa tu nombre (min 3 letras) y presiona Enter: ")
# dato = [{"Nombre": nombre}]

# juego = 1
# with open('datos.json') as file:
#     user = json.load(file)
#     if juego == 1:
#         for nombre in user["Jugadores"]:
#             try:
#                 print(nombre["Nombre"])
#                 # del nombre["Nombre"]
#                 user.clear()
#                 print("Aquí andamos")
#             except:
#                 pass
# user.insert(0,dato)
# print(user["Jugadores"])
# user["Jugadores"] = dato
# print(type(user))
# user["Jugadores"].append({"Nombre": "Txt"})

# with open('datos.json','w') as nuevo:
#     json.dump(user, nuevo, indent=4)