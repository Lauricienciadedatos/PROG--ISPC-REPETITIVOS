
mujeres = 0
varones = 0
mayores_de_edad = 0
menores_de_edad = 0

# Leer las edades y el sexo de 15 personas
for i in range(15):
    edad = int(input("Ingrese la edad de la persona {}: ".format(i + 1)))
    sexo = input("Ingrese el sexo de la persona {} (Mujer o Varón): ".format(i + 1)).lower()

    if sexo == "mujer":
        mujeres += 1
    elif sexo == "varón":
        varones += 1

    if edad >= 18:
        mayores_de_edad += 1
    else:
        menores_de_edad += 1

# Mostrar los resultados
print("Cantidad de mujeres:", mujeres)
print("Cantidad de varones:", varones)
print("Cantidad de personas mayores de edad:", mayores_de_edad)
print("Cantidad de personas menores de edad:", menores_de_edad)

