import json
import os
import random
os.system("cls")

with open("dataprueba.json", encoding='utf-8') as archivo:
    datos = json.load(archivo)

print(datos["Tema"])
ordenPreguntas = random.sample(range(len(datos["Valotario"])),10)
print(ordenPreguntas)