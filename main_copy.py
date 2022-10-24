import os
import random
os.system("cls")


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


# Lista de preguntas del 1 al 10 en desorden
preguntasAleatorias = random.sample(range(1, len(preguntas)+1), len(preguntas))

# print(preguntasAleatorias)

letrasRespuestas = []

for numero in preguntas:
    letrasDisponibles = []
    print(f"\n{numero}) {preguntas[preguntasAleatorias[numero-1]]}")
    print(respuestas[preguntasAleatorias[numero-1]])

    alternativasAleatorias = random.sample(range(0, len(alternativas[preguntasAleatorias[numero-1]])), len(alternativas[preguntasAleatorias[numero-1]]))
    for letra in range(len(alternativas[preguntasAleatorias[numero-1]])):
        print(f"    {chr(letra+97)}) {alternativas[preguntasAleatorias[numero-1]][alternativasAleatorias[letra]]}")
        letrasDisponibles.append(chr(letra+97))
        if alternativas[preguntasAleatorias[numero-1]][alternativasAleatorias[letra]] == respuestas[preguntasAleatorias[numero-1]]:
            # Almacena la alternativa correcta
            letrasRespuestas.append(chr(letra+97))

    while True:
        respuesta_Usuario = input("\n    Ingresa tu respuesta: ").lower()
        if respuesta_Usuario in letrasDisponibles:
            break

    # Comprueba si la respuesta es correcta
    if respuesta_Usuario == letrasRespuestas[numero-1]:
        print("\nRespuesta correcta")
    else:
        print("\nRespuesta incorrecta")



# for i in range(len(preguntas)):
#     letra_alternativa = []  # Almacena las alternativas disponibles
#     # Muestra la pregunta
#     print(f"\n{i+1}) {preguntas.get(preguntasAleatorias[i])}")
#     alternativasAleatorias = random.sample(range(0, len(alternativas[i+1])), len(alternativas[i+1]))  # lista de alternativas en desorden
#     print(alternativasAleatorias)

#     for j in range(len(alternativas[i+1])):  # Muestra las alternativas
#         print(f"    {chr(j+97)}) {alternativas[preguntasAleatorias[i]][alternativasAleatorias[j]]}")
#         # Añade la siguiente letra de alternativa "a", "b", "c", "d", ...
#         letra_alternativa.append(chr(j+97))
#         # Comprueba la alternativa correcta