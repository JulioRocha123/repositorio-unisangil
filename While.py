opcion = 0
print ("bienvenido a la calculadora")
print ("Menu \n1) Suma \n2) Resta \n3) Multipliación \n4) Divición \n5) potencia")
opcion = int(input("Elige una opción: "))
while opcion != 6:
    try:
        if opcion == 1:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            res = num1 + num2
            print ("El resultado de la suma es:", + res)
        elif opcion == 2:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            res = num1 - num2
            print ("resta")
        elif opcion == 3:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            res = num1 * num2
            print ("multiplicación")
        elif opcion == 4:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            res = num1 / num2
            print ("division")
        elif opcion == 5:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            res = num1 ** num2
            print ("potencia")
        elif opcion == 6:
            print ("salir")
    except ValueError:
        print("registra un valor diferente")
    else:
        print("digite un valor correcto")
        break


print ("gracias por usar la calculadora")
