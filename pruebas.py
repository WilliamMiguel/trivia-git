# import csv
import os
import pandas as pd
os.system("cls")
# os.chdir(r'C:\Users\WILLIAM\Documents\Bootcamp\TriviaGit')


# with open("PreguntasRespuestas.csv") as f:
#     datos = csv.reader(f, delimiter=";")
#     next(datos,None)
#     preguntas = []
#     alternativas = []
#     respuestas = []
#     for row in datos:
#         preguntas.append(row[0])
#         for alt in range(1,5):
#             alternativas.append(row[alt])
#         respuestas.append(row[5])
    
# print(preguntas)
# print(alternativas)
# print(respuestas)
print("\n-------------------------------------------------------\n")
datosP = pd.read_excel("PreguntasRespuestas.xlsx", engine="openpyxl" )
preguntas = datosP["Preguntas"]
alternativaA = datosP["Alternativa a"]
alternativaB = datosP["Alternativa b"]
alternativaC = datosP["Alternativa c"]
alternativaD = datosP["Alternativa d"]
respuestas = datosP["Respuesta"]

print(list(respuestas))

# alternativas = [datosP["Alternativa a"],datosP["Alternativa b"],datosP["Alternativa c"],datosP["Alternativa d"]]
# print(len(alternativas))
# print("\n-------------------------------------------------------\n")
# print(alternativas)


# print("\n-------------------------------------------------------\n")

# print(dir(datos))

