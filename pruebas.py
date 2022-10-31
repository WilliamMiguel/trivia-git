import json
import os
import random
import re
os.system("cls")

# with open("datacopy.json", encoding='utf-8') as archivo:
#     info = json.load(archivo)

def esNumero(funcion):
    def auxiliar(entrada):
        funcion(entrada)
        while entrada != "" and len(list(entrada)) > 2 or not entrada.isnumeric() or int(entrada) == 0:
            entrada = input("Ingresa un valor entre 0 y 9: ")
        return entrada
    return auxiliar

@esNumero
def pedirValores(valor):
    return valor

dato = "0"
dato3= pedirValores(dato)

print(dato3)






# ----CLASE PREGUNTA----------------------------

# class Pregunta:
#     def __init__(self, enunciado: str, alternativas: list, respuesta: str):
#         self.__enunciado = enunciado
#         self.__alternativas = alternativas
#         self.__respuesta = respuesta
#         self.__clave = ""
#         self.__letras = []

#     def Pregunta(self):
#         return self.__enunciado

#     def Alternativas(self):
#         random.shuffle(self.__alternativas)
#         for alternativa in self.__alternativas:
#             self.__letras.append(chr(self.__alternativas.index(alternativa)+97))
#             print(f"    {chr(self.__alternativas.index(alternativa)+97)}) {alternativa}")
#             if alternativa == self.__respuesta:
#                 self.__clave = chr(self.__alternativas.index(alternativa)+97)

#     def alternativaCorrecta(self):
#         usuarioAlternativa = input("Ingrese su respuesta: ").lower()
#         while usuarioAlternativa not in self.__letras:
#             usuarioAlternativa = input("Ingrese su respuesta: ").lower()
#         if usuarioAlternativa == self.__clave:
#             print("\nRespuesta correcta\n")
#             return True
#         else:
#             print("\nRespuesta incorrecta\n")

# listaPreguntas = []

# for cuestionario in info:
#     enunciado = cuestionario["Pregunta"]
#     alternativas = cuestionario["Alternativas"]
#     respuesta = cuestionario["Respuesta"]
#     pregunta = Pregunta(enunciado,alternativas,respuesta)
#     listaPreguntas.append(pregunta)

# # Lista de preguntas del 1 al 10 en desorden
# random.shuffle(listaPreguntas)

# numeroPreguntas = 10
# for pregunta in listaPreguntas:
#     if listaPreguntas.index(pregunta) == numeroPreguntas:
#         break
#     print(f"{listaPreguntas.index(pregunta)+1}) {pregunta.Pregunta()}")
#     pregunta.Alternativas()
#     print("")
#     pregunta.alternativaCorrecta()


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
