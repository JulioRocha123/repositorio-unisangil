# se le da la bienvenida al usuario 
print ("Bienvenido a la calculadora de terrenos con forma de triangulos")
# el ususario ingresa los datos de la base y la altura del terreno en forma triangular
B = float(input("Escribe la base del triangulo: "))
H = float(input("Escribe la altura del triangulo: "))
#se hace la operacion para hallar el area del terreno en forma triangular
A = float((B * H) / 2)
# Se mostrara al usuario el resulado de la operacion y se despedira al ususario
print ("EL area del triangulo es:",(A), "metros cuadrados")
print ("gracias por usar nuestra calculadora, !Feliz Día!")