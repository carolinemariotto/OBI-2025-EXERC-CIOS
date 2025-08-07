import sys

cartas = list(map(int, sys.stdin.readline().split()))

if cartas == sorted(cartas):
    print("C")
elif cartas == sorted(cartas, reverse=True):
    print("D")
else:
    print("N")
    