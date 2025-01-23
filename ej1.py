#Ejercicio 1: ordenar una lista de numeros ingresados por el usuario (Bubble sort)
#Instrucciones:

#Solicitar al usuario que ingrese 6 numeros separados por espacios
#Usa el metodo de ordenacion burbuja para organizarlos de menos a mayor
#Muestre la lista ordenada

numeros = input("Ingrese 6 numeros separados por espacios").split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

n = len(numeros)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]


print(f"La lista ordenada es: {numeros}")