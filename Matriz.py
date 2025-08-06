import pandas as pd

matriz1 = pd.read_excel("matriz1.xlsx", header=None).values
matriz2 = pd.read_excel("matriz2.xlsx", header=None).values

print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)

def matriz_quadrada(matriz):
    return matriz.shape[0] == matriz.shape[1]

if not (matriz_quadrada(matriz1) and matriz_quadrada(matriz2)):
    print("Erro: As matrizes não são quadradas!")
    exit()

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

n = matriz1.shape[0]
resultado = [[0]*n for _ in range(n)]

print("\nPasso a passo da multiplicação:\n")
for i in range(n):
    for j in range(n):
        soma_temp = 0
        for k in range(n):
            mult = multiplicacao(matriz1[i][k], matriz2[k][j])
            soma_temp = soma(soma_temp, mult)
            print(f"resultado[{i}][{j}] += {matriz1[i][k]} * {matriz2[k][j]}  => {soma_temp}")
        resultado[i][j] = soma_temp
    print()

print("Resultado da multiplicação de matrizes:")
for linha in resultado:
    print(linha)
