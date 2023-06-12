numeros_positivos = []

# Leer 15 números negativos
for i in range(5):
    numero = int(input("Ingrese un número negativo: "))

    # Convertir el número a positivo y agregarlo a la lista
    numero_positivo = abs(numero)
    numeros_positivos.append(numero_positivo)

# Mostrar los números positivos
print("Números positivos:")
for numero_positivo in numeros_positivos:
    print(numero_positivo)
