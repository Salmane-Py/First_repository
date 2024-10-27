
print()
print("Ce programme vous permez d'effectuer des convertions")
print("""
1- Pouces vers Cm
2- Cm vers Pouces
3- Quitter
""")

choix = input("Faites votre choix (1 / 2 / 3): ")

if choix == "1":
    valeur = float(input("Entrer une valeur en pouce: "))
    print("Votre résultat est "+ str(valeur*2.54) + " cm" )
    
elif choix == "2":
    valeur = float(input("Entrer une valeur en CM: "))
    print("Votre résultat est " + str(valeur*0.394) + " pouce" )

elif choix == "3":
    quit



#repeat = input("Veux-tu effectuer une autre convertion (oui/non): ")