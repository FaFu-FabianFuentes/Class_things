import os
import time
os.system ("cls")
#inicio valorizacion de cosas -------------------------------------------------------
opcion_menu    =("")
opcion_compra  =("")
nombre_cliente =("")
cata n       =29990
dixit        =19990
exploding_kit=19990


cant_catan     =0
cant_dixit     =0
cant_explo_kit =0

suma_catan     =0
suma_dixit     =0
suma_explo_kit =0

total = 0
total=suma_catan+suma_dixit+suma_explo_kit

#------------------------------------------------------------------------------------

nombre_cliente = str(input('''
            bienvenido ingrese su nombre para continuar:
            '''))



while True:
    os.system("cls")
    opcion_menu = str(input('''
           --------------- tienda de juguetes-------------------
           1.- Comprar
           2.- Total & salir
           
           
           Ingrese opción de menú:     '''))     
    if opcion_menu == "1":
        opcion_compra = str(input('''
           --------------- tienda de juguetes-------------------
                nombre producto             valor
           1.- Catán                        $29990
           2.- Dixit                        $19990
           3.- Exploding kittens            $19990
           4.- salir
           
            Ingrese opción de menú:     '''))
        if opcion_compra==("1"): 
            cant_catan = int(input(f'''
            Ingrese cantidad de Catán a comprar :
            valor por unidad : {catan}     '''))
            suma_catan = cant_catan*catan
        elif opcion_compra==("2"): 
            cant_dixit = int(input(f'''
            Ingrese cantidad de Dixit a comprar :
            valor por unidad : {dixit}     '''))
            suma_dixit= cant_dixit*dixit
        elif opcion_compra==("3"):
            cant_explo_kit = int(input(f'''
            Ingrese cantidad de Exploding kittens a comprar :
            valor por unidad : {exploding_kit}     '''))
            suma_explo_kit= cant_explo_kit*exploding_kit
        elif opcion_compra ==("4"):
            break
        else:
            print ("error : objeto pedido no ubicado")
    elif opcion_menu==("2"):
        total=total=suma_catan+suma_dixit+suma_explo_kit
        os.system("cls")
        print(f'''
              usted {nombre_cliente} lleva : 
              {cant_catan}      catanes             = ${suma_catan}
              {cant_dixit}      dixits              = ${suma_dixit}
              {cant_explo_kit}  exploding kittens   = ${suma_explo_kit}
              
              _________________________________
              ${total} es el total de su compra
              
              Gracias {nombre_cliente} por su compra!

              presione cualquier boton para continuar''')
        os.system("pause")
        print('''hasta la proxima :D...
                ''')
        time.sleep (100)
        os.system("cls")
        break
    else:
        print ("error : objeto pedido no ubicado")

