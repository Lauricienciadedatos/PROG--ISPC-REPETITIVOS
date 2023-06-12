
    # Ingresar 4 números

for i in range(4):
        numero = int(input("Ingrese un número: "))
        
        # Verificar si el número es par o impar

        if numero % 2 == 0:
            pares += 1
            sumatoria_pares += numero

        elif numero % 2 == 1:
             impares += 1
             sumatoria_impares += numero
             

    # Mostrar los resultados

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Sumatoria de números pares:", sumatoria_pares)

