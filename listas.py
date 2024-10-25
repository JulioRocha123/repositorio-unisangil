#Estrutura de una lista, los numeros no necesitan comillas ni los datos boleanos
#necesitan comillas los strings o caracteres
x = [101,"mama","s",False,4.8]
print (f"los datos de la lista son: {x}") #print (x) muestra la lista en general
print (f"el dato numero 1 es: {x[0]}")
print (f"el dato numero 1 de atras para adelante es: {x[-1]}") #el numero negativo en una lista es que esta es el valor inverso, osea de derecha a izquierda
print (f"el dato numero 4 de derecha a izquieda es: {x[-4]}")
#para recorrer una lista es (iniciolista):(hasta donde recorre la lista)
print (f"la lista de 101 a s {x[0:3]}")
print (x[0:])# si se deja solo los dos puntos: se imprime desde el inico hasta el final de la lista
print (f"la lista con numeros negativos es: {x[-4:-1]}") #si se desea ver una lista en orden negativo primero va de menor a mayor siendo el mayor el numero mas cercano a 0
#agregar datos a la lista
b = [1,5]
b.append (100) #.append se utliza para añadir datos a la lista pero se añaden en la ultima posicion
b.append ("julitorocha247@gmail.com")#.append se utiliza para cualquier tipo de variable
#tamaño lista
longitud = b.__len__() #.len ayuda a identificar el tamaño de la lista
print (f"el tamaño de la lista es {longitud}")
#.insert ayuda a que se puedan insertar numeros en la lista
b.insert(2,"rocha")# la estructura es: (posicion a ingresar),(dato que se va a añadir)
print (b)
b.insert(1,"X")
print (b)
b.insert(5,1034780288)
print (b)
b.append(10)
b.append(20)
longitud = b.__len__()
print (b)
print (f"el tamaño de la lista tras añadirle mas datos es: {longitud}")
#reemplazar datos de la lista
b[-3] = "julitogamer124@gmail.com" #la estructura para reemplazar datos es: posicion de donde se reemplaza = dato por el cual se reemplazara
print (b)
b.remove (100)#. remove se utiliza para remover datos de la lista (se necesita el dato especifico)
print (b)
b.pop () #.pop elimina el ultimo elemento de la lista no es necesario el dato especifico
print (b)
b[5:] = [] # se utiliza para eliminar datos o secciones en especifico
print (b)

#estructura de for para imprimir datos de la lista
u = -1
for i in b:
    u += 1
    print (f"el dato en la posicion {u} = {i}")
#invertir datos de la lista
b.reverse() #.reverse se utiliza para revertir la lista
c = -1
for i in b:
    c += 1
    print (f"el dato en la posicion {c} = {i}")
#ordenar datos
r = [10,8,20,6,80]
large = r.__len__()
print (r)
r.sort() #.sort ayuda a organizar los datos de menor a mayor y si o si tiene que hacer afuera de un print
print (f"la lista ordenada de menor a mayor utilizando .sort es: {r}")
print (f"urilizando el metodo sorted() la lista queda: {sorted(r)}") #en cambio sorted se puede utilizar dentro de un print y este se organizara de menor a mayor
r.sort(reverse = True) #el parametro reverse=true se utiliza para organizar los numeros de mayor a menor y si o si tiene que hacer afuera de un print
print (f"la lista ordenada de mayor a menor utilizando .sort(reverse=true) es: {r}")
suma = 0
for i in r:
    v = (suma + i) / large
    print (v)