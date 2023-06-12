
numeros = []
mayores_100 = 0
menores_100 = 0

    # Leer los 10 números
for i in range(10):
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)

        # Verificar si el número es mayor o menor a 100
        if numero > 100:
            mayores_100 += 1
        elif numero < 100:
            menores_100 += 1

    # Encontrar el número máximo y mínimo
maximo = max(numeros)
minimo = min(numeros)

    # Mostrar los resultados
print("Cantidad de números mayores a 100:", mayores_100)
print("Cantidad de números menores a 100:", menores_100)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)




 
