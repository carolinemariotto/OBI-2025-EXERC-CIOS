import sys 

N, M = list(map(int, sys.stdin.readline().split()))
matriz = []
contador = 0 

for _ in range(N): # primeiro crio um laço que vai ler a linha na matrix 
     linha = list(map(int, sys.stdin.readline().split()))
     matriz.append(linha)
     
X = int(sys.stdin.readline()) #variavel que vai ler os numeros

for i in range(N):
     for j in range(M):
          if matriz[i][j] == X:
               contador += 1
          print(contador)


