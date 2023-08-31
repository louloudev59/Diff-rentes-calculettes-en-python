
operateur = input("Quel opérateur souhaites-tu ? \n Merci de répondre soit un +, soit un -, soit un *, soit un / :")
if operateur == "+":
    print("Nous ferons donc une addition")
    
elif operateur == "-":
        print("Nous ferons donc une soustraction")
        
elif operateur == "/":
            print("Nous ferons donc une division")
        
elif operateur == "*":
                print("Nous ferons donc une multiplication")
else:
    print("Merci de choisir un caractère valide !".title())
nombre_1 = int(input("Choisissez un premier nombre :"))
nombre_2 = int(input("Choisissez un deuxième nombre :"))   
if operateur == "+":
    resultat = nombre_1 + nombre_2
elif operateur == "-":
    resultat = nombre_1 - nombre_2
elif operateur == "/":
    resultat = nombre_1 / nombre_2
else :
    resultat = nombre_1 * nombre_2
print(f"Le résultat de {nombre_1} {operateur} {nombre_2} est égale à {resultat}")
