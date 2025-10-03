import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))     

melhor = 1 
atual = 1

for i in range(1,N):
     if seq[i] == seq[i-1]:
          atual += 1
     else:
          if atual > melhor:  
               melhor = atual
          atual = 1
          
if atual > melhor:
     melhor = atual
print(melhor)

