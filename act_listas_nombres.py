import os
import time
os.system("cls")
opc_menu=("")
n=[]
while True :
    opc_menu = str(input('''
                Sistema de nombres :
                
                1-ingresar nombres
                2-revisar datos ingresados
                3-buscar nombre en lista
                4 salir
                
                '''))
    if opc_menu == 1:
        while (len(n)) <= 6:
            print("ingrese 6 nombres:")
            n.append(input(""))

    if opc_menu == 2:
        print("nombres ingresados :")
        for i in range(len(n)):
            time.sleep(1)
            n.sort()
            print(n[i])

    if opc_menu == 3:
        print("ingrese cual numero de la lsita desea buscar :")
        print(n[i-1])

    if opc_menu == 4:
        break
        


