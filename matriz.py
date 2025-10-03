import sys

# Primeiro, precisamos criar uma matriz vazia para preenchê-la com os dados da entrada.
matriz = []
contador = 0 

for _ in range(N):
     linhas = list(map(int,sys.stdin.readline().split()))
     matriz.append(linhas)

X = int(sys.stdin.readline())
contador2 = 0

for i in range(N):
     for j in range(M):
          if matriz[i][j] == X:
               contador2 += 1
print(contador2)
     


