import json
import time
import re
import random
import os
from colorama import Fore, init
init(autoreset=True)
os.system("cls")

#Importa las preguntas
with open("datacopy.json", encoding='utf-8') as archivo:
    info = json.load(archivo)

# Función para efecto de sorteo de número - ruleta
def efectoAleatorio():
    '''Realiza un efecto de elegir un número aleatorio'''
    tiempoInicio = time.time()
    duracion = 0
    while duracion < 1.5:
        print(random.randint(0, 9), end='\r')
        tiempoFin = time.time()
        duracion = tiempoFin - tiempoInicio

#DECORADOR PARA CONFIRMAR NÚMERO
def esNumero(funcion):
    def auxiliar(entrada):
        funcion(entrada)
        while entrada != "" and len(list(entrada)) > 1 or not entrada.isnumeric() or int(entrada) == 0:
            entrada = input(Fore.YELLOW + "Ingresa un valor entero entre 0 y 10: ")
        entrada = int(entrada)
        return entrada
    return auxiliar

@esNumero
def puntos(valor):
    return valor

print(Fore.BLUE + "Bienvenido a mi trivia sobre la Reforma Protestante\nPondre a prueba tus conocimientos históricos\n")

time.sleep(2)

patronNombre = re.compile('[a-z]+[a-z]+[a-z]')

while True:
    nombre = input("Ingresa tu nombre (min 3 letras) y presiona Enter: ")
    dato = re.search(patronNombre, nombre)
    if nombre != "" and type(dato) == re.Match:
        break

cantidadPreguntas = int(input("Ingresa la cantidad de preguntas que quieres responder: "))

print(Fore.BLUE + f'''\nHola {nombre}, responde las siguientes preguntas escribiendo la letra de la alternativa y presionando Enter para enviar tu respuesta.
Cada vez que aciertes una respuesta sumarás puntos, de lo contrario los perderás.''')

time.sleep(2)

# El usuario ingresa los puntos con los que quiere jugar
puntos_pos = input(Fore.GREEN + "Ingresa los puntos a sumar por respuesta correcta: ")
puntos_pos = puntos(puntos_pos)
puntos_neg = input(Fore.RED + "Ingresa los puntos a restar por respuesta incorrecta: ")
puntos_neg = puntos(puntos_neg)
puntaje_Inicial = 0
numero_intentos = []
puntaje_intentos = []
intentos = 1

while True:
    print(Fore.MAGENTA + f"\nIntento N° {intentos}")
    puntos_intento = []  # Almacena la puntuación en cada intento
    random.shuffle(info)
    for numero, cuestionario in enumerate(info):
        if numero == cantidadPreguntas:
            break
        letras = []  # Lista para las alternativas disponibles
        clave = ""  # Almacena la alternativas correctas
        print(Fore.CYAN + "\n" + str(numero+1) + ") " + cuestionario["Pregunta"]) # Muestra la pregunta
        random.shuffle(cuestionario["Alternativas"]) #Desordena las alternativas
        for letra, alternativa in enumerate(cuestionario["Alternativas"]): #Muestra las alternativas
            print("    " + chr(letra + 97) + ") " + alternativa)
            letras.append(chr(letra + 97)) #Añade una alternativa disponible
            if alternativa == cuestionario["Respuesta"]: #Guarda la alternativa correcta
                clave = chr(letra + 97)
        print("")
        while True:
            time.sleep(0.25)
            respuesta_Usuario = input("    Ingresa tu respuesta: ").lower()
            if respuesta_Usuario in letras:
                break
        if respuesta_Usuario == clave: # Comprueba si la respuesta es correcta
            print(Fore.GREEN + "\nRespuesta correcta")
            puntos_intento.append(puntos_pos)
        else:
            print(Fore.RED + "\nRespuesta incorrecta")
            puntos_intento.append(-puntos_neg)

    # -------------Fin de Preguntas------------------------------------

    if sum(puntos_intento) == puntos_pos * cantidadPreguntas:
        print(Fore.MAGENTA +
              "\n¡FELICITACIONES! Eres un crack en los temas de la Reforma")

    print(Fore.YELLOW + "\nAumentaremos el puntaje con números aleatorios")
    ruleta = input(Fore.YELLOW + "\n¿Cuántas veces quieres sortear el numero? Ingresa un número entero mayor a 0: ")
    ruleta = puntos(ruleta)

    for i in range(ruleta):
        numeroRuleta = random.randint(0, 9)
        print(Fore.LIGHTBLUE_EX + f"\nSorteo N° {i+1}:")
        efectoAleatorio()
        print(Fore.GREEN + f"    {numeroRuleta} punto(s)")

    puntaje_intentos.append(sum(puntos_intento) + numeroRuleta) # Puntaje en cada intento
    numero_intentos.append(intentos)  # Cantidad de intentos

    print(
        f"\n{Fore.YELLOW}Obtuviste {round(puntaje_intentos[intentos-1],2)} puntos en tu intento N° {numero_intentos[intentos-1]}")

    while True:
        repetir = input("\nPara finalizar escribe 0. Para volver a jugar escribe 1: ")
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
        for cuestionario in info:
            if info.index(cuestionario) == cantidadPreguntas:
                break
            print(Fore.CYAN + cuestionario["Pregunta"])
            print(Fore.LIGHTGREEN_EX + "   " + cuestionario["Respuesta"] + "\n")

        print("--------------------------------------\n")
        print(Fore.RED + f"Gracias por jugar {nombre}. Hasta pronto\n")
        break

    intentos += 1
