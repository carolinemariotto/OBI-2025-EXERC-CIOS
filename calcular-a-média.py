import sys 

prova = int(input(sys.stdin.readline))
nota = 10

media = prova + nota / 2 

if media > 7:
    print("Aprovado")
    
elif media < 7:
    print("Ainda um pouco")
    
else:
     print("Reprovado")

