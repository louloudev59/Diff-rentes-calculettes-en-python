
nombre_1 = input("Merci de choisir un premier nombre :")
while not nombre_1.isdigit():
    nombre_1 = input("Merci de choisir un premier nombre (entier) :")
nombre_2 = input("Merci de choisir un deuxième nombre :")
while not nombre_2.isdigit():
    nombre_2 = input("Merci de choisir un deuxième nombre (entier) :")
nombre_1 = int(nombre_1)
nombre_2 = int(nombre_2)
print(f"Le résultat de {nombre_1} + {nombre_2} est de {nombre_1 + nombre_2}")
