"""
un estudiate realiza cuatro examenes durante el semestre ayudalo a encontrar el promedio de las notas
se le pide al estudante que ingrese las 4 notas que obtuvo 
"""
c1 = float(input("Ingresa la nota de la primera calificacion: "))
c2 = float(input("Ingresa la nota de la segunda calificacion: "))
c3 = float(input("Ingresa la nota de la tercera calificacion: "))
c4 = float(input("Ingresa la nota de la cuarta calificacion: "))
# Aqui se hace la operacion de la suma para mostrarle el resultado al estudante
s = c1 + c2 + c3 + c4
# Se le muestra al estudainte la suma de las notas
print("la suma de tus calificaciones es: ", (s))
# Se hace la operacion para hallar el promedio de las notas
p = s/4
# Se le muestra al estudiante el promedio que obtuvo y se despide al estudiante
print("el promedio de tus calificaciones es: ", (p))
print("Muchas Gracias por usarnos, !Feliz Día!")