""" 
1. recorrer array 3->4->6->5->7->2->1

3. guardar datos de a pares ejem: (3 y 4)

para iteracion en array 

#intecambiar valores
si x > y:

    x = valor recorrido del array
    y = el siguiente numero del array (x + 1)
    
 si se cumple:
 
    temporal = x (se usa una variable temporal para no perder el valor de x)
    x = y (asigna el valor de y a x)
    y = temporal (asigna el valor de temporal 
    
repetir el proceso

imprimir resultado del nuevo array ordenado

"""

arr = [3, 4, 6, 5, 7, 2, 1]

n = len(arr)

for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        
print(arr)
    
