"""

"""
#se importa la libreria math
import math
#se definen las variables fijas del primer punto
eficienciaP = 0.15
radiacionS = 5
Apanel = 1.6
potencia_diaria = (Apanel * radiacionS * eficienciaP) #se calcula la potencia diaria y se muestra al ususario
print ("la potencia diaria es: ", potencia_diaria, "kWh")
potencia_anual = potencia_diaria * 365 #se calcula pa potencia anual y se le muestra al usuario
print ("la potencia anual es: ", potencia_anual, "kWh")
consumo1 = 12000 / potencia_anual # se calcula cantidad de paneles solares
nredondeado = math.ceil(consumo1) # se usan las funciones math.ceil para redonder el numero a entero
print ("se necesita una cantidad de: ", nredondeado," paneles solares para un consumo anual de 12000 kWh\n")
print("Extra\n ")
# se le permite al usuario ingresar datos
EficienciaU = float(input("Ingresa la eficiencia del panel solar en decimal: "))
RadiacionU = float(input("Ingresa la Radicación solar por metro cuadrado del panel solar: "))
TamañoU = float(input("Ingresa el tamaño del panel solar: "))
HorasU = float(input("Ingresa las horas de uso del panel solar: "))
#Se realiza la operacion para calcular la potencia anual segun los datos ingresados por el ususario
PotenciaA = (TamañoU * RadiacionU * EficienciaU)*365
print ("La potencia anual es: ",PotenciaA, "\n") #se muestra el resultado con un salto de linea
#se le pide el usuasrio que ingrese datos 
ConsumoU = float(input("Ingresa el consumo anual: "))
PotenciaU = float(input("Ingresa la potencia anual: "))
#se calcula la cantidad de paneles
panel1 = ConsumoU / PotenciaU
#se redondea el numero de paneles a entero usando la funcion math.ceil
rpanel = math.ceil(panel1)
print ("se necesita una cantidad de: ", rpanel," paneles solares para un consumo anual de", ConsumoU," kWh")
#se calcula el area que utilizaran los paneles
AreaTU = rpanel * Apanel
print ("Se necesita un area de: ", AreaTU, "metros cuadrados")