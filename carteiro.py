import sys

n, m = map(int, sys.stdin.readline().split())
casas = list(map(int, sys.stdin.readline().split()))
encomendas = list(map(int, sys.stdin.readline().split()))   

posicao_atual = 0
tempo_total = 0

for destino in encomendas:
     for i, n in enumerate(casas):
        if n == destino:
          tempo_total += abs(i - posicao_atual)
          posicao_atual = i
          print(tempo_total)   