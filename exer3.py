import sys

N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

soma = [0] * (N + 1)

for i in range(N):
    soma[i + 1] = soma[i] + A[i]

for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    
    soma_intervalo = soma[R + 1] - soma[L]    
    print(soma_intervalo) 