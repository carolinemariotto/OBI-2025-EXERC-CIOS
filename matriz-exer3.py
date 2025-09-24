import sys 

N = list(map(int, sys.stdin.readline().split()))
M = list(map(int, sys.stdin.readline().split()))
matriz = [2, 2]

for _ in range(2, 0, -1):
     linha = list(map(int, sys.stdin.readline().split()))
     matriz.append(N)
     
contador = list(map(int, sys.stdin.readline().split()))
for i in range(N):
     for j in range(M):
          if matriz[i][j] == contador:
               contador += 1
          print(contador)