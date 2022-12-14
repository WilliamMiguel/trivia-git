import time, re, random, os
from colorama import Fore, init
init(autoreset=True)
os.system("cls")

# #Función para efecto de sorteo de número - ruleta
# def efectoAleatorio():
#     '''Realiza un efecto de elegir un número aleatorio'''
#     tiempoInicio = time.time()
#     duracion = 0
#     while duracion < 1.5:
#         print(random.randint(0, 9), end='\r')
#         tiempoFin = time.time()
#         duracion = tiempoFin - tiempoInicio

# #Función para asignar los puntos a restar o sumar
# def puntaje(puntos: str):
#     '''Ingresa "acumular" o "restar"'''
#     while True:
#         puntuacion = input(Fore.YELLOW + f"Ingresa los puntos a {puntos}: ")
#         if puntuacion != "" and puntuacion.replace('.', '', 1).isnumeric() and float(puntuacion) > 0:
#             puntuacion = float(puntuacion)
#             break
#         print("Ingresa un valor numérico y mayor a 0 ...")
#     return puntuacion

# print(Fore.BLUE + "Bienvenido a mi trivia sobre la Reforma Protestante\nPondre a prueba tus conocimientos históricos\n")

# time.sleep(2)

# patronNombre = re.compile('[a-z]+[a-z]+[a-z]')

# while True:
#     nombre = input("Ingresa tu nombre (min 3 letras) y presiona Enter: ")
#     dato = re.search(patronNombre, nombre)
#     if nombre != "" and type(dato) == re.Match:
#         break

# print(Fore.BLUE + f'''\nHola {nombre}, responde las siguientes preguntas escribiendo la letra de la alternativa y presionando Enter para enviar tu respuesta.
# Cada vez que aciertes una respuesta sumarás puntos, de lo contrario los perderás.''')

# time.sleep(2)

# # El usuario ingresa los puntos con los que quiere jugar
# puntos_pos = puntaje("acumular")
# puntos_neg = puntaje("restar")
# puntaje_Inicial = 0

import json
with open("data.json", encoding='utf-8') as archivo:
    datos = json.load(archivo)

letrasRespuestas = []  # Almacena las alternativas correctas
puntos_intento = []  # Almacena la puntuación en cada intento

# Lista de preguntas del 1 al 10 en desorden
ordenPreguntas = random.sample(range(1, len(datos)+1), len(datos))
for numero in datos:
    letrasDisponibles = []  # Almacena las alternativas disponibles
    # Muestra la pregunta
    print("\n"+numero+")",datos[str(ordenPreguntas[int(numero)-1])]["Pregunta"])

    #Almacena cuántas alternativas existen
    cantidadAlternativas = len(datos[str(ordenPreguntas[int(numero)-1])]["alternativas"])
    #Lista para desordenar las alternativas
    ordenAlternativas = random.sample(range(0, cantidadAlternativas), cantidadAlternativas)
    for letra in range(cantidadAlternativas):  # Muestra las alternativas
        print("    " + chr(letra+97) + ")", datos[str(ordenPreguntas[int(numero)-1])]["alternativas"][letra])
        # Guarda la siguiente letra de alternativa "a", "b", "c", "d", ...
        letrasDisponibles.append(chr(letra+97))
        # Comprueba la alternativa correcta
        if datos[str(ordenPreguntas[int(numero)-1])]["alternativas"][letra] == datos[str(ordenPreguntas[int(numero)-1])]["Respuesta"]:
            # Almacena la alternativa correcta
            letrasRespuestas.append(chr(letra+97))



# numero_intentos = []
# puntaje_intentos = []
# intentos = 1

# while True:
#     print(Fore.MAGENTA + f"\nIntento N° {intentos}")

#     letrasRespuestas = []  # Almacena las alternativas correctas
#     puntos_intento = []  # Almacena la puntuación en cada intento

#     # Lista de preguntas del 1 al 10 en desorden
#     preguntasAleatorias = random.sample(range(1, len(preguntas)+1), len(preguntas))

#     for numero in preguntas:
#         letrasDisponibles = []  # Almacena las alternativas disponibles
#         # Muestra la pregunta
#         print(Fore.CYAN + f"\n{numero}) {preguntas[preguntasAleatorias[numero-1]]}")

#         alternativasAleatorias = random.sample(range(0, len(alternativas[preguntasAleatorias[numero-1]])), len(alternativas[preguntasAleatorias[numero-1]]))
#         for letra in range(len(alternativas[preguntasAleatorias[numero-1]])):  # Muestra las alternativas
#             print(f"    {chr(letra+97)}) {alternativas[preguntasAleatorias[numero-1]][alternativasAleatorias[letra]]}")
#             # Añade la siguiente letra de alternativa "a", "b", "c", "d", ...
#             letrasDisponibles.append(chr(letra+97))
#             # Comprueba la alternativa correcta
#             if alternativas[preguntasAleatorias[numero-1]][alternativasAleatorias[letra]] == respuestas[preguntasAleatorias[numero-1]]:
#                 # Almacena la alternativa correcta
#                 letrasRespuestas.append(chr(letra+97))

#         while True:
#             time.sleep(0.25)
#             respuesta_Usuario = input("\n    Ingresa tu respuesta: ").lower()
#             if respuesta_Usuario in letrasDisponibles:
#                 break

#         # Comprueba si la respuesta es correcta
#         if respuesta_Usuario == letrasRespuestas[numero-1]:
#             print(Fore.GREEN + "\nRespuesta correcta")
#             puntos_intento.append(puntos_pos)
#         else:
#             print(Fore.RED + "\nRespuesta incorrecta")
#             puntos_intento.append(-puntos_neg)

#     #-------------Fin de Preguntas------------------------------------

#     if sum(puntos_intento) == puntos_pos * len(preguntas):
#         print(Fore.MAGENTA + "\n¡FELICITACIONES! Eres un crack en los temas de la Reforma")

#     print(Fore.YELLOW + "\nAumentaremos el puntaje con números aleatorios")
#     while True:
#         ruleta = input(Fore.YELLOW + "\n¿Cuántas veces quieres sortear el numero? Ingresa un número entero mayor a 0: ")
#         if ruleta != "" and ruleta.isnumeric() and float(ruleta) > 0:
#             ruleta = int(ruleta)
#             break

#     for i in range(ruleta):
#         numeroRuleta = random.randint(0, 9)
#         print(Fore.LIGHTBLUE_EX + f"Sorteo N° {i+1}:")
#         efectoAleatorio()
#         print(Fore.GREEN + f"    {numeroRuleta} punto(s)")

#     # Puntaje en cada intento
#     puntaje_intentos.append(sum(puntos_intento) + numeroRuleta)

#     # Cantidad de intentos
#     numero_intentos.append(intentos)

#     print(f"\n{Fore.YELLOW}Obtuviste {round(puntaje_intentos[intentos-1],2)} puntos en tu intento N° {numero_intentos[intentos-1]}")

#     while True:
#         repetir = input("\nPara finalizar escribe 0. Para volver a jugar escribe 1: ")
#         if repetir != "" and repetir.replace('.', '', 1).isnumeric() and (float(repetir) == 0 or float(repetir) == 1):
#             repetir = int(repetir)
#             break

#     if repetir == 0:
#         #Se muestran los puntajes por intentos
#         print("\n--------------------------------------\n")
#         for i in numero_intentos:
#             print(Fore.MAGENTA + f"Intento N° {numero_intentos[i-1]}: {puntaje_intentos[i-1]} puntos")
#         print("\n--------------------------------------\n")
        
#         #Se muestran las respuestas
#         time.sleep(1)
#         print(Fore.LIGHTMAGENTA_EX +"Las respuestas correctas son:\n")
#         for i in preguntas:
#             print(Fore.CYAN + preguntas.get(i))
#             print(Fore.LIGHTGREEN_EX + f"   {respuestas.get(i)}\n")

#         print("--------------------------------------\n")
#         print(Fore.RED + f"Gracias por jugar {nombre}. Hasta pronto\n")
#         break

#     intentos += 1