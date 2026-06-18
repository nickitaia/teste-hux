n = int(input())
l1 = []
for i in range(n):
    l1.append(int(input()))
l2 = []
for i in range(n):
    l2.append(int(input()))
resultado = []
for i in range(n):
    resultado.append(l1[i])
    resultado.append(l2[i])
for n in resultado:
    print(n)