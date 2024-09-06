"""
N = necesario
"""
#consumo diario
import math

eficienciaP = 0.15
radiacionS = 5
Apanel = 1.6
potencia_diaria = (Apanel * radiacionS * eficienciaP)
print ("la potencia diaria es: ", potencia_diaria, "kWh")
potencia_anual = potencia_diaria * 365
print ("la potencia anual es: ", potencia_anual, "kWh")
consumo1 = 12000 / potencia_anual
nredondeado = math.ceil(consumo1)
print ("se necesita una cantidad de: ", nredondeado," paneles solares para un consumo anual de 12000 kWh")
print("Extra")
