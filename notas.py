import sys
notas = list(map(int, sys.stdin.readline().strip().split()))
notas.sort()
print(notas)
