import json
import os
import random
os.system("cls")

with open("dataprueba.json", encoding='utf-8') as archivo:
    datos = json.load(archivo)

# letrasRespuestas = []
# ordenPreguntas = [i for i in range(len(datos["Valotario"]))]
# random.shuffle(ordenPreguntas)
# for indice, pregunta in enumerate(ordenPreguntas):
#     print("\n" + str(indice+1) + ") " + datos["Valotario"][pregunta]["Pregunta"])
#     ordenAlternativas = [i for i in range(len(datos["Valotario"][pregunta]["Alternativas"]))]
#     random.shuffle(ordenAlternativas)
#     for letra, alternativa in enumerate(ordenAlternativas):
#         print("    " + chr(letra+97) + ") " + datos["Valotario"][pregunta]["Alternativas"][alternativa]) 
#         if datos["Valotario"][pregunta]["Alternativas"][alternativa] == datos["Valotario"][pregunta]["Respuesta"]:
#             # Almacena la alternativa correcta
#             letrasRespuestas.append(chr(letra+97))

for i in range(len(datos["Valotario"])):
    print(datos["Valotario"][i]["Pregunta"])
    print("   "+datos["Valotario"][i]["Respuesta"]+"\n")