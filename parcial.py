"""
Julio rocha
Liceth Rodriguez
Marcy Castro
"""
saldo = 10000
pinu = int(input("ingrese el pin: "))
pin = 1234
error = 0
intx = 2
while pinu != pin:
    print("pin incorrecto")
    intm = intx + 1
    pin = int(input("Ingrese el pin: "))
    if pinu == pin:
        while pinu == pin:
            print ("Menú \n1) Consultar saldo \n2) Realizar deposito \n3) Realizar retiro \n4) Salir")
            menu = int(input("Ingrese la opcion a elegir: "))
            if menu == 1:
                print ("Tu saldo es de: ", saldo)
            elif menu == 2:
                depo = int(input("Ingrese el deposito: "))
                saldo = depo + saldo
                print ("Tu saldo es de: ", saldo)
            elif menu == 3:
                ret = int(input("Ingrese el valor a retirar: "))
                if ret > saldo:
                    print ("saldo insuficiente")
                else:
                    saldo = saldo - ret
                print ("posee un saldo de: ", saldo)
            elif menu >= 4:
                print ("gracias por elegirnos")
            break
else:
    error = error + 1
    print ("contraseña incorrecta, vuelva a ingresar el pin")

