import sys 

N = list(map(int, input().split()))
M = list(map(int, input().split()))
matriz = []
contador = 0

for _ in range(N):
     linhas = list(map(int, sys.stdin.readline().split()))
     matriz.append(linhas)
     
maior_soma =  -float('inf')
indice = -1

for i in range(N):
     soma = sum(matriz[i])
     
     if soma > maior_soma:
          maior_soma = soma
          indice = i
print(indice)