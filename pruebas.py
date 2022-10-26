import json
import os
os.system("cls")

with open("data.json", encoding='utf-8') as archivo:
    datos = json.load(archivo)

print(datos[str(1)]["Pregunta"])
