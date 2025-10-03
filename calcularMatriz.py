import sys 

N, M = map(int, sys.stdin.readline().split())
matriz = []

for _ in range(N):
     linhas = list(map(int, sys.stdin.readline().split()))
     matriz.append(linhas)

x = int(sys.stdin.readline())
contador = 0

for i in range(N):
     for j in range(M):
          if matriz[i][j] == x:
               contador += 1
print(contador)
               
          
               
               
