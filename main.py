import json
import time
import re
import random
import os
from colorama import Fore, init
init(autoreset=True)
os.system("cls")

# Función para efecto de sorteo de número - ruleta


def efectoAleatorio():
    '''Realiza un efecto de elegir un número aleatorio'''
    tiempoInicio = time.time()
    duracion = 0
    while duracion < 1.5:
        print(random.randint(0, 9), end='\r')
        tiempoFin = time.time()
        duracion = tiempoFin - tiempoInicio

# Función para asignar los puntos a restar o sumar


def puntaje(puntos: str):
    '''Ingresa "acumular" o "restar"'''
    while True:
        puntuacion = input(Fore.YELLOW + f"Ingresa los puntos a {puntos}: ")
        if puntuacion != "" and puntuacion.replace('.', '', 1).isnumeric() and float(puntuacion) > 0:
            puntuacion = float(puntuacion)
            break
        print("Ingresa un valor numérico y mayor a 0 ...")
    return puntuacion


print(Fore.BLUE + "Bienvenido a mi trivia sobre la Reforma Protestante\nPondre a prueba tus conocimientos históricos\n")

time.sleep(2)

patronNombre = re.compile('[a-z]+[a-z]+[a-z]')

while True:
    nombre = input("Ingresa tu nombre (min 3 letras) y presiona Enter: ")
    dato = re.search(patronNombre, nombre)
    if nombre != "" and type(dato) == re.Match:
        break

print(Fore.BLUE + f'''\nHola {nombre}, responde las siguientes preguntas escribiendo la letra de la alternativa y presionando Enter para enviar tu respuesta.
Cada vez que aciertes una respuesta sumarás puntos, de lo contrario los perderás.''')

time.sleep(2)

# El usuario ingresa los puntos con los que quiere jugar
puntos_pos = puntaje("acumular")
puntos_neg = puntaje("restar")
puntaje_Inicial = 0

with open("dataprueba.json", encoding='utf-8') as archivo:
    datos = json.load(archivo)

numero_intentos = []
puntaje_intentos = []
intentos = 1
numeroPreguntas = 10

while True:
    print(Fore.MAGENTA + f"\nIntento N° {intentos}")

    letrasRespuestas = []  # Almacena las alternativas correctas
    puntos_intento = []  # Almacena la puntuación en cada intento

    # Lista de preguntas del 1 al 10 en desorden
    ordenPreguntas = random.sample(range(len(datos["Valotario"])),10)
    random.shuffle(ordenPreguntas)

    for indice, pregunta in enumerate(ordenPreguntas):
        letrasDisponibles = []  # Almacena las alternativas disponibles
        # Muestra la pregunta
        print(Fore.CYAN + "\n" + str(indice+1) + ") " + datos["Valotario"][pregunta]["Pregunta"])

        # Desordenar las alternativas
        ordenAlternativas = [i for i in range(len(datos["Valotario"][pregunta]["Alternativas"]))]
        random.shuffle(ordenAlternativas)

        for letra, alternativa in enumerate(ordenAlternativas):  # Muestra las alternativas
            print("    " + chr(letra+97) + ") " + datos["Valotario"][pregunta]["Alternativas"][alternativa])
            # Guarda la siguiente letra de alternativa "a", "b", "c", "d", ...
            letrasDisponibles.append(chr(letra+97))
            # Comprueba la alternativa correcta
            if datos["Valotario"][pregunta]["Alternativas"][alternativa] == datos["Valotario"][pregunta]["Respuesta"]:
                # Almacena la alternativa correcta
                letrasRespuestas.append(chr(letra+97))

        while True:
            time.sleep(0.25)
            respuesta_Usuario = input("\n    Ingresa tu respuesta: ").lower()
            if respuesta_Usuario in letrasDisponibles:
                break

        # Comprueba si la respuesta es correcta
        if respuesta_Usuario == letrasRespuestas[indice]:
            print(Fore.GREEN + "\nRespuesta correcta")
            puntos_intento.append(puntos_pos)
        else:
            print(Fore.RED + "\nRespuesta incorrecta")
            puntos_intento.append(-puntos_neg)

    # -------------Fin de Preguntas------------------------------------

    if sum(puntos_intento) == puntos_pos * len(datos["Valotario"]):
        print(Fore.MAGENTA +
              "\n¡FELICITACIONES! Eres un crack en los temas de la Reforma")

    print(Fore.YELLOW + "\nAumentaremos el puntaje con números aleatorios")
    while True:
        ruleta = input(
            Fore.YELLOW + "\n¿Cuántas veces quieres sortear el numero? Ingresa un número entero mayor a 0: ")
        if ruleta != "" and ruleta.isnumeric() and float(ruleta) > 0:
            ruleta = int(ruleta)
            break

    for i in range(ruleta):
        numeroRuleta = random.randint(0, 9)
        print(Fore.LIGHTBLUE_EX + f"Sorteo N° {i+1}:")
        efectoAleatorio()
        print(Fore.GREEN + f"    {numeroRuleta} punto(s)")

    # Puntaje en cada intento
    puntaje_intentos.append(sum(puntos_intento) + numeroRuleta)

    # Cantidad de intentos
    numero_intentos.append(intentos)

    print(
        f"\n{Fore.YELLOW}Obtuviste {round(puntaje_intentos[intentos-1],2)} puntos en tu intento N° {numero_intentos[intentos-1]}")

    while True:
        repetir = input(
            "\nPara finalizar escribe 0. Para volver a jugar escribe 1: ")
        if repetir != "" and repetir.replace('.', '', 1).isnumeric() and (float(repetir) == 0 or float(repetir) == 1):
            repetir = int(repetir)
            break

    if repetir == 0:
        # Se muestran los puntajes por intentos
        print("\n--------------------------------------\n")
        for i in numero_intentos:
            print(
                Fore.MAGENTA + f"Intento N° {numero_intentos[i-1]}: {puntaje_intentos[i-1]} puntos")
        print("\n--------------------------------------\n")

        # Se muestran las respuestas
        time.sleep(1)
        print(Fore.LIGHTMAGENTA_EX + "Las respuestas correctas son:\n")
        for i in ordenPreguntas:
            print(Fore.CYAN + datos["Valotario"][i]["Pregunta"])
            print(Fore.LIGHTGREEN_EX + "   "+datos["Valotario"][i]["Respuesta"]+"\n")

        print("--------------------------------------\n")
        print(Fore.RED + f"Gracias por jugar {nombre}. Hasta pronto\n")
        break

    intentos += 1
