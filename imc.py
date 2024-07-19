import math as mt

ALTURA = float(input("Digite sua altura: "))
PESO = float(input("Digite seu peso atual: "))

IMC = PESO/(ALTURA ** 2)

if(IMC <= 16.9):
    print("Classificação:")
    print("Muito abaixo do peso")

elif(17 <= IMC <= 18.4):
    print("Classificação:")
    print("Abaixo do peso")

elif(18.5 <= IMC <= 24.9):
    print("Classificação:")
    print("Peso normal")

elif(25 <= IMC <= 29.9):
    print("Classificação:")
    print("Acima do peso")

elif(30 <= IMC <= 34.9):
    print("Classificação:")
    print("Obesidade grau I")

elif(35 <= IMC <= 40):
    print("Classificação:")
    print("Obesidade grau II")

elif(IMC >= 40):
    print("Classificação:")
    print("Obesidade grau III")
