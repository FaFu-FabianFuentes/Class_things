import os
import time
os.system("cls")

n=[]

while (len(n)) <= 6:
    print("ingrese nombre:")
    n.append(input(""))


print("nombres ingresados :")
for i in range(len(n)):
    time.sleep(1)
    n.sort()
    print(n[i])
