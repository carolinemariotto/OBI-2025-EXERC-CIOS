import sys 

n = int((input())) #tamanho da sequencia 
# sequencia de 0 e uns separados por espaço
m = list(map(int, input().split()))

contador = 0
# programa deve imprimir um inteiro, mas algumas vezes o padrão "100" aparece na sequência.
for i in range(n-2):
     if m[i] == 1 and m[i+1] == 0 and m[i+2] == 0:
          contador += 1
print(contador)