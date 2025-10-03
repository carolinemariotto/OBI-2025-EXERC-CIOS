import sys

N = int(sys.stdin.readline())

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    qtd = N // nota   # quantas notas dessa cabem
    print(f"{qtd} nota(s) de {nota}")
    N = N % nota      # atualiza o que sobrou
