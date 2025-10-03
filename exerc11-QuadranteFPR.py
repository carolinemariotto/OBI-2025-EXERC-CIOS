import sys 

X = int(input("Digite o valor de X: "))
E = int(input("Digite o valor de E: "))

for eixo in range(1,4):
     if X > 0 and E > 0:
       print("Q1")
       break
     elif X < 0 and E > 0:
          print("Q2")
          break
     elif X < 0 and E < 0:
          print("Q3")
          break
     elif X > 0 and E < 0:
          print("Q4")
          break
     else:
          print("Eixos ")
          break
