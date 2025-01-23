#Complejidad algoritmica y metodos de ordenacion
#(Bubble sort e insertion sort)

#Cuando trabajamos con algoritmos es fundamental evaluar que tan eficientes son en 
#terminos de ejecucion y uso de memoria. Esta eficiencia se mide mediante la complejiad algoritmica.
#Esto nos ayuda a estimar el comportamiendo del algoritmo cuando el tamaño de los datos crece


#La complejidad algoritmica mide los recursos que necesita un algoritmo para ejecutarse y se mide en terminos de:

#Tiempo de ejecucion o complejidad temporal
#Cuanto tiempo toma ejecutar el algoritmo en funcion de la cantidad de los datos de entrada (n) se suele expresas en
#una notacion llamada big o o(n), o(n2), o(log n)

#Uso de la memoria o complejidad espacial:
#Cuanta memoria adicional requiere el algoritmo para ejecutarse
#Tambien se expresa en Big o

#Notacion Big o
#Describir como crece el tiempo de ejecucion de un algoritmo en relacion a su tamaño de entrada. Alguno de los ordenes 
#de complejidad mas comunes son:

#O(1): Tiempo constante(rapido). ejemplo acceso a un elemento de un arreglo... no importa cuan grande sea la entrada, el tiempo es constante
#o(log n): tiempo logartirmica. ejemplo busqueda binaria... 
#O(n): tiempo lineal. ejemplo recorrido un arreglo
#O(n2): tiempo cuadratico (lento). Ejemplo ordenacion por burbuja

#Como ordenar...

#Es el proceso de organizar elemenetos en un orden especifico, por ejemplo (ascendente y descendente)
#Existen multiples algoritmos, cada uno con sus ventajas y desventajas sobre todo en terminos de eficiencia 

#Ordenacion por burbuja o bubble sort
#Este algoritmo comprar elemento adyoacentes y los cambia se estan en el orden incorrecto, esto se repite hasta
#que no se necesiten mas intercambios

#Este algoritmo en el mejor de los casos es lineas, en el peor es cuadratico y espacialmente hablando es constante 

numeros = [5, 3, 8, 4, 2]
n = len(numeros)

for i in range(n - 1)):
    for j in range(n- 1 - i):
        if numeros [j] > numeros [j + 1]:
            temp = numeros[j]
            numeros[j] = numeros [j + 1]
            numeros[j + 1] = temp
print(f"lista ordnada con bubble sort: {numeros}")

#Ventajas
#Facil de entender e implementar
#Funciona bien con listas pequeñas

#Desventajas
#Ineficiente para listas grandes 
#Realiza muchas comparaciones que son inecesarias


#Metodo de ordenacion por insercion 
 
#Consntruye una lista ordenada de manera incremental, insertando cada elemento en la posicion 
#correcta respecto a los ya ordenados

#En el mejor de los casos es lineal
#En el peor de los casos es cuadratico 
#Especialmente hablando es constante 

num = [7, 3, 5, 2, 6]
n = len(num)

for i in range(1 , n):
    clave = num[i]
    j = i - 1
    while j >= 0 and num[j] > clave:
        num[j + 1] = num[j]
        j -= 1
    num[j + 1] = clave

print(f"Lista ordenada con insertion: {num}")

