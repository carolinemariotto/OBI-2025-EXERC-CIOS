import sys 

s = list(map(int, input().split()))
contador = 0

for i in s:
     if s[i+1] > s[i]:
          print(s[i+1])
     else: 
          print(s[i+2])