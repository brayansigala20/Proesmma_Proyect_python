# nombres = """brayan sigala, jose martinez, pablo montero, luis torres"""

# NOMBRES_1 = nombres[0:13]
# NOMBRES_2 = nombres[15:]

# print(f"{NOMBRES_1} y  {NOMBRES_2}")

# calculadora

# num1 = input('Ingresa el primer numero ')
# num2 = input('Ingresa el segun numero ')

# edad = 56

# if edad > 65:
#    print("tienes un super descuento")

# elif edad > 55:
#    print("tienes un descuento")

# elif edad > 18:
#    print("puedes entrar")
# else:
#    print("no puedes entrar")

# condicionales ternarios
# EDAD = 20
# MENSAJE = "Es mayor" if EDAD >= 18 else "Es menor"
# print(MENSAJE)

# operadores logicos and not or

# AGE = 18
# DRIVE_CARD = False
# DRIVE_COURSE = True

# if AGE >= 18 and DRIVE_CARD and DRIVE_COURSE:
#     print("puede conducir sin problema")

# if AGE >= 18 and not (DRIVE_CARD and DRIVE_COURSE):
#     print("puede conducir pero no cuenta con la total aprobacion")

# if AGE < 18 and not (DRIVE_CARD and DRIVE_COURSE):
#     print("no puede")


# Cadena de comparacion

# import pandas as pd
# AGE = 25

# Simplify chained comparison between the operands (esto es un error de slint y dice que se puede simplificar)
# if AGE >= 18 and AGE <= 60:
#     print("puede pasar")

# # aqui la manera simplificada ya que solo ocupa una variable
# if 18 <= AGE <= 60:
#     print("puede pasar")

# lista = ['pepe', 'jose', 'lalo', 'pedro']

# for index in lista:
#     print(index)

# # Funcion con xArgument paramentro iterable

# def new_function(*numbers):
#     res = 0
#     for number in numbers:
#         res = number * 2
#     return res


# print(new_function(5, 4, 5))

# # Funcion con kwArgument paramentro

# def new_function(**numbers):
#     print(numbers["n1"])


# new_function(n1=5, n2=4, n3=5)


# Palindromo

# def is_palindromo(string):
#     string_formated = string.lower().replace(" ", "")

#     if string_formated == "".join(reversed(string_formated)):
#         return "es Palindromo"
#     return "no es palindromo"


# print(is_palindromo("ana ana"))

mascotas = ["perro", "gato", "camaleon", "serpiente"]

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
