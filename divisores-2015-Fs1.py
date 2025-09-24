import sys 

def divisores(n):
    if n < 1:
        return 0
    cont = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cont += 1
    return cont

print(divisores(int(sys.stdin.readline())))