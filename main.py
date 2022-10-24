import time, re, random, os
from colorama import Fore, init
init(autoreset=True)
os.system("cls")

#Función para efecto de sorteo de número - ruleta
def efectoAleatorio():
    '''Realiza un efecto de elegir un número aleatorio'''
    tiempoInicio = time.time()
    duracion = 0
    while duracion < 1.5:
        print(random.randint(0, 9), end='\r')
        tiempoFin = time.time()
        duracion = tiempoFin - tiempoInicio

#Función para asignar los puntos a restar o sumar
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

#El usuario ingresa los puntos con los que quiere jugar
puntos_pos = puntaje("acumular")
puntos_neg = puntaje("restar")
puntaje_Inicial = 0

preguntas = {
    1: "¿En qué año inició la Reforma Protestante?",
    2: "¿Quién inició la Reforma Protestante?",
    3: "¿En qué año murió Martín Lutero?",
    4: "¿Por qué Martín Lutero ingresó al monasterio?",
    5: "¿En qué país tuvo sus inicios la Reforma Protestante?",
    6: "¿Cuál fue el tema central por el cual se dió la Reforma?",
    7: "¿Qué fuentes de revelación especial considera la iglesia católica romana?",
    8: "De los siguientes lemas, uno fue parte de la batalla de la Reforma, ¿cuál es?",
    9: "¿Quién dijo: Puedes quemar este ganso, si así lo quieren, pero vendrá después de mí un cisne, a quien no podrán silenciar?",
    10: "¿Cuántas tesis clavó Lutero en la iglesia de Todos los Santos de Wittenberg?"
}

alternativas = {
    1: ["1605", "1517", "1532", "1455"],
    2: ["Cristóbal Colón", "Leonardo da Vinci", "Martín Lutero", "René Descartes"],
    3: ["1546", "1500", "1605", "1515"],
    4: ["Quería ser santo", "Le gustaba estudiar la Biblia", "Hizo una promesa a una santa", "Sus papás le obligaron"],
    5: ["Perú", "España", "Alemania", "Inglaterra"],
    6: ["La iglesia", "Los papas", "La santificación", "La justificación"],
    7: ["La iglesia", "Los santos", "La costumbre", "Ninguna de las alternativas"],
    8: ["Post Tenebras Lux", "Sola Scriptura", "Sola Gratia", "Coram Deo"],
    9: ["Juan Huss", "Juan Calvino", "Martín Lutero", "John Knox"],
    10: ["85 tesis", "95 tesis", "90 tesis", "93 tesis"]
}

respuestas = {
    1: "1517",
    2: "Martín Lutero",
    3: "1546",
    4: "Hizo una promesa a una santa",
    5: "Alemania",
    6: "La santificación",
    7: "Ninguna de las alternativas",
    8: "Sola Scriptura",
    9: "Juan Huss",
    10: "95 tesis"}

numero_intentos = []
puntaje_intentos = []
intentos = 1

while True:
    print(Fore.MAGENTA + f"\nIntento N° {intentos}")

    letrasRespuestas = []  # Almacena las alternativas correctas
    puntos_intento = []  # Almacena la puntuación en cada intento

    # Lista de preguntas del 1 al 10 en desorden
    preguntasAleatorias = random.sample(range(1, len(preguntas)+1), len(preguntas))

    for numero in preguntas:
        letrasDisponibles = []  # Almacena las alternativas disponibles
        # Muestra la pregunta
        print(Fore.CYAN + f"\n{numero}) {preguntas[preguntasAleatorias[numero-1]]}")

        alternativasAleatorias = random.sample(range(0, len(alternativas[preguntasAleatorias[numero-1]])), len(alternativas[preguntasAleatorias[numero-1]]))
        for letra in range(len(alternativas[preguntasAleatorias[numero-1]])):  # Muestra las alternativas
            print(f"    {chr(letra+97)}) {alternativas[preguntasAleatorias[numero-1]][alternativasAleatorias[letra]]}")
            # Añade la siguiente letra de alternativa "a", "b", "c", "d", ...
            letrasDisponibles.append(chr(letra+97))
            # Comprueba la alternativa correcta
            if alternativas[preguntasAleatorias[numero-1]][alternativasAleatorias[letra]] == respuestas[preguntasAleatorias[numero-1]]:
                # Almacena la alternativa correcta
                letrasRespuestas.append(chr(letra+97))

        while True:
            time.sleep(0.25)
            respuesta_Usuario = input("\n    Ingresa tu respuesta: ").lower()
            if respuesta_Usuario in letrasDisponibles:
                break

        # Comprueba si la respuesta es correcta
        if respuesta_Usuario == letrasRespuestas[numero-1]:
            print(Fore.GREEN + "\nRespuesta correcta")
            puntos_intento.append(puntos_pos)
        else:
            print(Fore.RED + "\nRespuesta incorrecta")
            puntos_intento.append(-puntos_neg)

    #-------------Fin de Preguntas------------------------------------

    if sum(puntos_intento) == puntos_pos * len(preguntas):
        print(Fore.MAGENTA + "\n¡FELICITACIONES! Eres un crack en los temas de la Reforma")

    print(Fore.YELLOW + "\nAumentaremos el puntaje con números aleatorios")
    while True:
        ruleta = input(Fore.YELLOW + "\n¿Cuántas veces quieres sortear el numero? Ingresa un número entero mayor a 0: ")
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

    print(f"\n{Fore.YELLOW}Obtuviste {round(puntaje_intentos[intentos-1],2)} puntos en tu intento N° {numero_intentos[intentos-1]}")

    while True:
        repetir = input("\nPara finalizar escribe 0. Para volver a jugar escribe 1: ")
        if repetir != "" and repetir.replace('.', '', 1).isnumeric() and (float(repetir) == 0 or float(repetir) == 1):
            repetir = int(repetir)
            break

    if repetir == 0:
        #Se muestran los puntajes por intentos
        print("\n--------------------------------------\n")
        for i in numero_intentos:
            print(Fore.MAGENTA + f"Intento N° {numero_intentos[i-1]}: {puntaje_intentos[i-1]} puntos")
        print("\n--------------------------------------\n")
        
        #Se muestran las respuestas
        time.sleep(1)
        print(Fore.LIGHTMAGENTA_EX +"Las respuestas correctas son:\n")
        for i in preguntas:
            print(Fore.CYAN + preguntas.get(i))
            print(Fore.LIGHTGREEN_EX + f"   {respuestas.get(i)}\n")

        print("--------------------------------------\n")
        print(Fore.RED + f"Gracias por jugar {nombre}. Hasta pronto\n")
        break

    intentos += 1