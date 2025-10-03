#basico-medio exercicio-2
import sys

N, M = list(map(int, sys.stdin.readline().split()))

matriz = [N, M]
contador = 0

for i in range(2):
     for j in range(2):
          if matriz[i][j] > 10:
               contador += 1
print(contador)
#basico-medio exercicio-2