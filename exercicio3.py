import sys 

N1, D2, V2 = map(int, sys.stdin.readline().split())

N2, D2, V2 = map(int, sys.stdin.readline().split())

total1 =  D1 / V1
total2 =  D2 / V2

if total1 < total2:
    print("N1") 
else:
    print("N2")
