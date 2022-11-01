import json
import time
import re
import random
import os
from colorama import Fore, init
init(autoreset=True)
os.system("cls")

# Importa las preguntas
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

# DECORADOR PARA CONFIRMAR NÚMERO


def numeroValido(funcion):
    def auxiliar(entrada, valorcero, limite):
        funcion(entrada, valorcero, limite)
        if not valorcero:  # Para valorcero = False
            while not entrada.isnumeric() or entrada == "0" or int(entrada) > limite:
                entrada = input(f"Ingresa un número entero positivo válido: ")
            entrada = int(entrada)
            return entrada
        else:
            while not entrada.isnumeric() or int(entrada) != 1 and int(entrada) != 0:
                entrada = input(f"Ingresa 0 o 1: ")
            entrada = int(entrada)
            return entrada
    return auxiliar


@numeroValido
def puntos(entrada, cero: bool, limite):
    '''True para comprobar 0 y 1. False para comprobar otro número. Límite: valor máximo aceptable'''
    return entrada, cero, limite


print(Fore.BLUE + "Bienvenido a mi trivia sobre la Reforma Protestante\nPondre a prueba tus conocimientos históricos\n")

time.sleep(2)

patronNombre = re.compile('[a-z]+[a-z]+[a-z]')

while True:
    nombre = input("Ingresa tu nombre (min 3 letras) y presiona Enter: ")
    dato = re.search(patronNombre, nombre)
    if nombre != "" and type(dato) == re.Match:
        break

cantidadPreguntas = input(f"Ingresa la cantidad de preguntas que quieres responder (máx. {len(info)}): ")
cantidadPreguntas = puntos(cantidadPreguntas, False, len(info))
puntos_pos = 1
puntos_neg = 1

print(Fore.BLUE + f'''\nHola {nombre}, responde las siguientes preguntas escribiendo la letra de la alternativa y presionando Enter para enviar tu respuesta.
Cada vez que aciertes una respuesta sumarás {Fore.GREEN}{puntos_pos} punto{Fore.RESET}{Fore.BLUE}, de lo contrario lo perderás.''')

time.sleep(2)

# El usuario ingresa los puntos con los que quiere jugar
# puntos_pos = input(Fore.GREEN + "Ingresa los puntos a sumar por respuesta correcta: ")
# puntos_pos = puntos(puntos_pos, False, None)
# puntos_neg = input(Fore.RED + "Ingresa los puntos a restar por respuesta incorrecta: ")
# puntos_neg = puntos(puntos_neg, False)
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
        print(Fore.CYAN + "\n" + str(numero+1) + ") " +
              cuestionario["Pregunta"])  # Muestra la pregunta
        # Desordena las alternativas
        random.shuffle(cuestionario["Alternativas"])
        # Muestra las alternativas
        for letra, alternativa in enumerate(cuestionario["Alternativas"]):
            print("    " + chr(letra + 97) + ") " + alternativa)
            letras.append(chr(letra + 97))  # Añade una alternativa disponible
            # Guarda la alternativa correcta
            if alternativa == cuestionario["Respuesta"]:
                clave = chr(letra + 97)
        print("")
        while True:
            time.sleep(0.25)
            respuesta_Usuario = input("    Ingresa tu respuesta: ").lower()
            if respuesta_Usuario in letras:
                break
        if respuesta_Usuario == clave:  # Comprueba si la respuesta es correcta
            print(Fore.GREEN + "\nRespuesta correcta")
            puntos_intento.append(puntos_pos)
        else:
            print(Fore.RED + "\nRespuesta incorrecta")
            puntos_intento.append(-puntos_neg)

    # -------------Fin de Preguntas------------------------------------
    print("\n--------------------------------------")
    puntajeprevio = sum(puntos_intento)
    if puntajeprevio < 0:
        print(f"{Fore.LIGHTRED_EX}Acumulaste {puntajeprevio} punto(s)")
    else:
        print(f"{Fore.LIGHTGREEN_EX}Acumulaste {puntajeprevio} punto(s)")
    print("--------------------------------------\n")

    if sum(puntos_intento) == puntos_pos * cantidadPreguntas:
        print(Fore.MAGENTA + "¡FELICITACIONES! Eres un crack en los temas de la Reforma")

    print(Fore.YELLOW + "Aumentaremos el puntaje con números aleatorios")
    ruleta = input(Fore.YELLOW + "\n¿Cuántas veces quieres sortear el numero? Ingresa un número entero mayor a 0: ")
    ruleta = puntos(ruleta, False, 10)

    for i in range(ruleta):
        numeroRuleta = random.randint(0, 9)
        print(Fore.LIGHTBLUE_EX + f"\nSorteo N° {i+1}:")
        efectoAleatorio()
        print(Fore.GREEN + f"    {numeroRuleta} punto(s)")

    # Puntaje en cada intento
    puntaje_intentos.append(sum(puntos_intento) + numeroRuleta)
    numero_intentos.append(intentos)  # Cantidad de intentos

    print(f"\n{Fore.YELLOW}Tu puntaje final es: {round(puntaje_intentos[intentos-1],2)} puntos en tu intento N° {numero_intentos[intentos-1]}")

    repetir = input(Fore.BLUE + "\nPara finalizar escribe 0. Para volver a jugar escribe 1: ")
    repetir = puntos(repetir, True, 0)

    if repetir == 0:
        # Se muestran los puntajes por intentos
        print("\n--------------------------------------\n")
        for i in numero_intentos:
            print(Fore.MAGENTA + f"Intento N° {numero_intentos[i-1]}: {puntaje_intentos[i-1]} puntos")
        print("\n--------------------------------------\n")

        # Se muestran las respuestas
        time.sleep(1)
        print(Fore.LIGHTMAGENTA_EX +
              "Las respuestas correctas en tu último intento son:\n")
        for cuestionario in info:
            if info.index(cuestionario) == cantidadPreguntas:
                break
            print(Fore.CYAN + cuestionario["Pregunta"])
            print(Fore.LIGHTGREEN_EX + "   " +
                  cuestionario["Respuesta"] + "\n")

        print("--------------------------------------\n")
        print(Fore.RED + f"Gracias por jugar {nombre}. Hasta pronto\n")
        break

    intentos += 1
